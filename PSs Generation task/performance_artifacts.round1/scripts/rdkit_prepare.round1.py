#!/usr/bin/env python3
"""Validate a candidate manifest and prepare reproducible 3D conformers for ORCA.

Input CSV required columns: candidate_id,smiles,charge,multiplicity.
Raw input is never changed. Invalid or failed records remain in the output manifest.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd
from rdkit import Chem
from rdkit.Chem import AllChem, Crippen, Descriptors, Lipinski, rdMolDescriptors


def prepare(row: pd.Series, seed: int) -> tuple[dict, Chem.Mol | None]:
    result = row.to_dict()
    mol = Chem.MolFromSmiles(str(row.smiles))
    if mol is None:
        result.update(validity_status="invalid_smiles", failure_reason="RDKit parsing failed")
        return result, None
    canonical = Chem.MolToSmiles(mol, isomericSmiles=True)
    mol_h = Chem.AddHs(mol)
    params = AllChem.ETKDGv3()
    params.randomSeed = seed
    embed = AllChem.EmbedMolecule(mol_h, params)
    if embed != 0:
        result.update(validity_status="conformer_failed", failure_reason=f"ETKDGv3 status {embed}")
        return result, None
    try:
        optimize = AllChem.MMFFOptimizeMolecule(mol_h, mmffVariant="MMFF94s", maxIters=500)
    except Exception as exc:  # Metal complexes may not have MMFF parameters.
        optimize = -1
        result["optimization_warning"] = str(exc)
    result.update(
        canonical_smiles=canonical,
        validity_status="prepared" if optimize >= 0 else "prepared_unoptimized",
        failure_reason="",
        mmff_status=optimize,
        molecular_weight=Descriptors.MolWt(mol),
        clogp=Crippen.MolLogP(mol),
        tpsa=rdMolDescriptors.CalcTPSA(mol),
        rotatable_bonds=Lipinski.NumRotatableBonds(mol),
    )
    mol_h.SetProp("candidate_id", str(row.candidate_id))
    mol_h.SetProp("canonical_smiles", canonical)
    return result, mol_h


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output-csv", type=Path, required=True)
    parser.add_argument("--output-sdf", type=Path, required=True)
    parser.add_argument("--xyz-dir", type=Path, required=True)
    parser.add_argument("--seed", type=int, default=20260726)
    args = parser.parse_args()
    frame = pd.read_csv(args.input)
    required = {"candidate_id", "smiles", "charge", "multiplicity"}
    missing = required - set(frame.columns)
    if missing:
        raise ValueError(f"Missing input columns: {sorted(missing)}")
    if frame.candidate_id.duplicated().any():
        raise ValueError("candidate_id must be unique")
    args.output_csv.parent.mkdir(parents=True, exist_ok=True)
    args.output_sdf.parent.mkdir(parents=True, exist_ok=True)
    args.xyz_dir.mkdir(parents=True, exist_ok=True)
    records, molecules = [], []
    seen = set()
    for _, row in frame.iterrows():
        record, molecule = prepare(row, args.seed)
        canonical = record.get("canonical_smiles")
        if canonical and canonical in seen:
            record.update(validity_status="duplicate", failure_reason="duplicate canonical SMILES")
            molecule = None
        elif canonical:
            seen.add(canonical)
        if molecule is not None:
            xyz_path = args.xyz_dir / f"{row.candidate_id}.xyz"
            xyz_path.write_text(Chem.MolToXYZBlock(molecule), encoding="utf-8")
            record["xyz_path"] = str(xyz_path)
        records.append(record)
        molecules.append(molecule)
    pd.DataFrame(records).to_csv(args.output_csv, index=False)
    with Chem.SDWriter(str(args.output_sdf)) as writer:
        for molecule in molecules:
            if molecule is not None:
                writer.write(molecule)


if __name__ == "__main__":
    main()
