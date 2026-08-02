#!/usr/bin/env python3
"""Write one auditable, proposed ORCA input per prepared candidate.

This writes only new files in the requested output directory. It deliberately
requires an explicit charge/multiplicity table from the candidate manifest.
"""
from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


TEMPLATE = """# Round-1 screening profile; requires materials-expert benchmark approval.
! PBE0 D4 def2-SVP TightSCF Opt CPCM(Water)
%pal nprocs {nprocs} end
%maxcore {maxcore_mb}
%tddft
  nroots {nroots}
  triplets true
end
* xyz {charge} {multiplicity}
{xyz}*
"""


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--nprocs", type=int, default=8)
    parser.add_argument("--maxcore-mb", type=int, default=2500)
    parser.add_argument("--nroots", type=int, default=30)
    args = parser.parse_args()
    frame = pd.read_csv(args.manifest)
    required = {"candidate_id", "charge", "multiplicity", "xyz_path", "validity_status"}
    missing = required - set(frame.columns)
    if missing:
        raise ValueError(f"Missing manifest columns: {sorted(missing)}")
    args.output_dir.mkdir(parents=True, exist_ok=True)
    for row in frame[frame.validity_status.isin(["prepared", "prepared_unoptimized"])].itertuples():
        xyz_file = Path(row.xyz_path)
        if not xyz_file.is_file():
            raise FileNotFoundError(xyz_file)
        xyz = "\n".join(xyz_file.read_text(encoding="utf-8").splitlines()[2:]) + "\n"
        content = TEMPLATE.format(nprocs=args.nprocs, maxcore_mb=args.maxcore_mb, nroots=args.nroots, charge=int(row.charge), multiplicity=int(row.multiplicity), xyz=xyz)
        (args.output_dir / f"{row.candidate_id}.inp").write_text(content, encoding="utf-8")


if __name__ == "__main__":
    main()
