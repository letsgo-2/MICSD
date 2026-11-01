# Computer-Expert Supplement: DFT-Computable Metrics and Iterative Optimization

## 1. What is genuinely computable?

The optimization loop should operate in tiers:

- **Tier A — directly calculable molecular descriptors:** geometry, charge, dipole, frontier orbital energies, vertical excitation energies, oscillator strengths, singlet/triplet state energies, spin-density/localization, approximate redox potentials, reorganization energies, and selected aggregation energies.
- **Tier B — physics-informed proxies:** triplet-energy compatibility with oxygen sensitization, electron-transfer driving force, heavy-atom orbital contribution, and absorption-weighted light-capture proxies. These require calibrated methods and should be validated against measured data.
- **Tier C — experiment-only or separately learned endpoints:** `ΦΔ`, absolute ROS rates, phototoxic IC50/EC50, dark toxicity, phototherapeutic index, uptake/localization, photostability in cells, pyroptosis fraction, cytokine release, and immune response. DFT alone must not receive credit for these.

## 2. DFT/TD-DFT metrics

| Metric | Meaning | Calculation recipe | Unit / output | Optimization use | Main caveat |
|---|---|---|---|---|---|
| Ground-state geometry and conformer energy | Stable conformers and relative populations; affects conjugation, charge, aggregation, and excited states | Enumerate conformers; optimize with dispersion-corrected DFT; frequency check; implicit solvent; retain low-energy conformers | kcal/mol or kJ/mol; geometry | Hard validity filter and ensemble input | A single conformer is unsafe for flexible targeting groups and aggregates |
| HOMO/LUMO energies and gap | Approximate donor/acceptor orbital energetics and electronic softness; a screening descriptor, not an observable band gap by itself | Ground-state DFT with functional/basis appropriate to charge-transfer systems; report orbital convention and solvent | eV | Intermediate feature; weakly weighted proxy | Functional, self-interaction, and charge-transfer errors can be large; do not use a universal gap target |
| Vertical S0→Sn excitation energy | Franck–Condon electronic excitation at fixed nuclei; maps to absorption candidates | TD-DFT on optimized conformers with solvent model; use a range-separated/hybrid functional when charge transfer is important; inspect transition character | eV or nm | Primary computational proxy for excitation compatibility | TD-DFT functional and environment can shift spectra; compare only with matched protocol |
| Oscillator strength `f` | Dimensionless transition intensity; IUPAC defines it as a measure of integrated electronic-transition intensity | TD-DFT transition dipole/oscillator output; select the relevant state, not automatically S1 | dimensionless | Intermediate; can form an absorption-strength proxy with wavelength | Brightness does not imply ROS generation; aggregation and vibronic structure are omitted |
| T1 energy | Energy of lowest triplet state; controls whether energy transfer to oxygen is thermodynamically accessible | Optimize triplet state or use appropriately validated excited-state method; compare vertical and adiabatic definitions explicitly | eV | Type-II compatibility proxy or Type-I design feature | State ordering and method errors matter; triplet energy alone does not predict `ΦΔ` |
| `ΔE(S1–T1)` and singlet/triplet state character | Energy gap and orbital character relevant to ISC and Type-I/II pathway engineering | TD-DFT/TDA or multireference validation for near-degenerate states; inspect natural transition orbitals and state character | eV | Intermediate mechanistic descriptor | Small gap is not sufficient; ISC also depends on spin–orbit coupling and vibronic coupling |
| Spin–orbit coupling (SOC) matrix elements | Relativistic coupling enabling spin-forbidden transitions such as ISC | Relativistic TD-DFT or SOC-enabled excited-state calculation; use effective core potentials/relativistic Hamiltonian for heavy atoms | cm−1 or related | Intermediate/diagnostic for metal/heavy-atom scaffolds | Expensive and method-sensitive; SOC is not an ISC rate without energy-gap and coupling information |
| Transition density / natural transition orbitals / charge-transfer distance | Spatial separation and donor–acceptor character of excitation | TD-DFT NTO analysis, transition-density difference, electron–hole descriptors | Å, dimensionless overlap, or charge metric | Intermediate; distinguishes local excitation from ICT | Definitions and software implementations differ; calibrate to scaffold family |
| Dipole moment and partial charge distribution | Polarity, charge separation, and possible solvent/membrane interactions | Ground-state DFT; optionally excited-state dipole and electrostatic potential | Debye; e | Feature/constraint for solubility and targeting hypotheses | Does not directly predict membrane localization or aggregation |
| Vertical ionization / electron affinity and solution redox potentials | Electron-donor/acceptor strength and ET driving-force inputs | ΔSCF or calibrated frontier/total-energy approach with solvent and reference-electrode correction; compute neutral/cation/anion consistently | eV or V | Type-I and ET proxy | Absolute potentials require calibration and solvent/reference conventions; no universal cutoff |
| Photoinduced ET driving force | Thermodynamic favorability of photoinduced electron transfer with donor/acceptor | Combine excitation energy and redox potentials using an IUPAC-consistent free-energy expression; retain Coulomb/solvent terms | eV or kJ/mol | Type-I screening proxy | Favorability does not equal rate; reorganization and electronic coupling are required |
| Inner-sphere reorganization energy `λin` | Nuclear relaxation energy after vertical electron transfer | Optimize neutral and ionized states; four-point energy scheme; IUPAC defines reorganization energy as Gibbs energy dissipated during relaxation after vertical ET | eV | Type-I/ET proxy; lower can support faster ET in matched regime | Outer-sphere solvent contribution and Marcus inverted-region effects are not captured by a single scalar |
| Heavy-atom orbital contribution / NBO composition | Approximate structural contribution to ISC-promoting heavy-atom effect | NBO/NAO population on optimized structure and orbitals participating in the relevant TD-DFT transition; calibrated AHAC-like model | dimensionless contribution | Screening feature for halogenated/metal systems | A published model is scaffold- and dataset-limited; not a universal `ΦΔ` predictor |
| Dimer/stacking interaction energy | Aggregation tendency of representative pair geometries | Optimize monomer and π-stacked/offset dimers with dispersion and solvent; compare binding energies and geometries | kcal/mol or kJ/mol | Constraint/proxy for aggregation resistance | Pair choice, concentration, entropy, and larger aggregates matter |
| Predicted absorption-weighted capture proxy | Approximate photon capture relevant to a chosen light window | Combine TD-DFT oscillator strengths, predicted wavelengths, and an explicit target spectral weighting; validate against measured extinction coefficients | protocol-defined score | Secondary objective | Not an extinction coefficient unless calibrated; does not include tissue attenuation |

## 3. Recommended calculation tiers

### Fast screening

Conformer generation → dispersion-corrected ground-state optimization → solvent model → HOMO/LUMO, gap, dipole, charge, low-energy conformer energy → TD-DFT for first 10–20 states and oscillator strengths → NTO/charge-transfer classification.

### Mechanism-aware screening

Add triplet-state calculations, `S1/T1` character, approximate SOC for heavy atoms, ΔSCF redox potentials, ET driving force, and inner-sphere reorganization energy. Use a fixed protocol per scaffold family.

### Validation tier

Use higher-level or multireference checks for candidates with near-degenerate states, metal-centered/ligand-centered state mixing, strong charge transfer, or disagreement among functionals. Compare with measured absorption, `ΦΔ`, ROS identity, and phototoxicity before updating reward weights.

## 4. Metrics eligible for an iterative reward

### Eligible from the first computational cycle

1. **Validity constraints:** geometry convergence, no imaginary frequency for the selected minimum, acceptable charge/spin state, and no chemically invalid valence.
2. **Excitation-window score:** soft target around the selected illumination window using TD-DFT excitation energy and oscillator strength.
3. **Triplet compatibility score:** soft/diagnostic score based on calculated `T1` relative to the singlet-oxygen energy requirement, never a hard `ΦΔ` guarantee.
4. **ET driving-force score:** soft target for desired radical chemistry, only with consistent redox and solvent conventions.
5. **Reorganization-energy score:** lower or calibrated target within the intended ET regime.
6. **Aggregation proxy:** penalize strongly favorable dimer stacking or unstable conformer/charge states, with explicit geometry and solvent assumptions.
7. **SOC/heavy-atom feature:** secondary score for metal/heavy-atom candidates, calibrated only within a scaffold family.

### Not eligible as DFT-only rewards

`ΦΔ`, absolute ROS production, cellular IC50/EC50, dark toxicity, phototherapeutic index, cellular uptake, organelle localization, photostability in biological medium, pyroptosis fraction, GSDMD/GSDME cleavage, LDH, cytokines, and immune response. These can become rewards only after adding experimental data or a validated uncertainty-aware surrogate model.

## 5. Reward construction and threshold policy

Use normalized soft rewards, not brittle universal cutoffs:

```text
R = validity_gate * [
      w_absorption * band_score(lambda, f)
    + w_triplet * calibrated_triplet_score(T1)
    + w_ET * calibrated_ET_score(DeltaG_ET)
    + w_reorg * calibrated_reorganization_score(lambda_in)
    + w_aggregate * aggregation_penalty
    + w_SOC * family_calibrated_SOC_score
    ]
```

Recommended encodings:

- **Excitation window:** use a soft band, initially `600–800 nm` for conventional PDT design context, with `600–850 nm` retained as a broader phototherapeutic-window context from reviews. This is source-backed context, not a universal molecular cutoff; two-photon and Type-I strategies may change it.
- **Triplet oxygen sensitization:** use a thermodynamic compatibility check against the approximately `0.98 eV` singlet-oxygen energy quoted in the photophysics review, but do not turn it into a fixed `T1` reward without matching electronic-structure definitions. The Ma 2024 review reports method-dependent `3O2/1O2` gaps from about `0.98` to `1.75 eV`, demonstrating why a soft interval and method provenance are required.
- **Quantum yield:** do not set a DFT reward threshold for `ΦΔ`. The uploaded papers report `>0.33` and `up to 0.91` under different conditions; authoritative reviews explicitly warn that `ΦΔ` may not correlate directly with cellular photodynamic efficiency. Use measured `ΦΔ` only as a later calibrated objective.
- **Light-capture proxy:** if extinction coefficients are measured or reliably predicted, use `ε × Φ` as a conditional efficiency feature. One translational review describes approximately `100 M−1 cm−1` as a good and `1,000 M−1 cm−1` as excellent benchmark for a phototherapeutic quantum-efficiency product, but this is not a universal molecular threshold and should remain a soft reference.
- **Redox and reorganization:** no universal reward thresholds are accepted here. Use within-dataset quantile normalization or a mechanistic target derived from the intended donor/acceptor reaction and solvent.
- **Aggregation:** no universal dimer-binding cutoff. Penalize candidates relative to matched scaffold controls and include multiple stack geometries.
- **Biological endpoints:** use assay-specific measured baselines, uncertainty intervals, and Pareto optimization. Never back-propagate a single cell-line threshold into a DFT-only reward.

## 6. Minimum record for each computed candidate

SMILES/3D structure; protonation and charge; spin multiplicity; conformer set; functional/basis/ECP; dispersion correction; solvent model; temperature if used; state definition (vertical/adiabatic); TD-DFT state number; oscillator strength; NTO/state character; triplet method; redox reference; reorganization-energy convention; dimer geometry protocol; software/version; convergence diagnostics; and uncertainty or ensemble spread.

## 7. Authority and evidence

- IUPAC Gold Book: oscillator strength `O04339`; excitation energy `E02250`; Franck–Condon principle `F02510`; reorganization energy `R05292`; photoinduced electron-transfer Gibbs energy `GT07388`; IUPAC photochemistry glossary, DOI `10.1351/pac200779030293`.
- Homem-de-Mello et al., “Evaluation of computational approaches to design new photosensitizers,” DOI `10.21826/viiiseedmol2020-29`: emphasizes (TD-)DFT usefulness, functional selection, dispersion and solvation for aggregation, and limits for metal complexes.
- Ma et al., Advanced Science 2024, DOI `10.1002/advs.202413365`: Type-I design and method-dependent triplet/oxygen energy discussion.
- Makhseed et al. 2013, DOI `10.1039/c3cc44609c`; Machacek et al. 2015; Peng et al. 2021 DOI `10.1021/acsabm.1c00719`; Su et al. 2022 DOI `10.1002/anie.202115800`; Yu et al. 2022 DOI `10.1021/jacs.2c03256`; Yi et al. 2024 DOI `10.1021/jacs.4c01929`: uploaded primary evidence.
- Abrahamse and Hamblin 2016, PMC `PMC4811612`; Cui et al. 2024, PMC `PMC11510636`; “Taking phototherapeutics from concept to clinical launch,” PMC `PMC8493544`: phototherapeutic windows, quantum yields, extinction coefficients, and condition dependence.
