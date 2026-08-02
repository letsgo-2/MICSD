#!/usr/bin/env bash
# Submit only after setting ORCA_MODULE and PROJECT_DIR for the target cluster.
# The method is an unbenchmarked Round-1 screening proposal, not an expert-approved final protocol.
#SBATCH --job-name=orca-round1
#SBATCH --array=0-0
#SBATCH --cpus-per-task=8
#SBATCH --mem=24G
#SBATCH --time=24:00:00
#SBATCH --output=performance_artifacts.round1/logs/orca_%A_%a.out
#SBATCH --error=performance_artifacts.round1/logs/orca_%A_%a.err
set -euo pipefail

PROJECT_DIR="${PROJECT_DIR:?Set PROJECT_DIR to the project directory}"
ORCA_MODULE="${ORCA_MODULE:?Set ORCA_MODULE, e.g. orca/6.0.1}"
MANIFEST="${MANIFEST:-$PROJECT_DIR/performance_artifacts.round1/data/prepared_candidates.round1.csv}"
module load "$ORCA_MODULE"
mkdir -p "$PROJECT_DIR/performance_artifacts.round1/raw_orca" "$PROJECT_DIR/performance_artifacts.round1/logs"
candidate_id=$(python - "$MANIFEST" "$SLURM_ARRAY_TASK_ID" <<'PY'
import pandas as pd, sys
df = pd.read_csv(sys.argv[1])
df = df[df["validity_status"].isin(["prepared", "prepared_unoptimized"])].reset_index(drop=True)
print(df.loc[int(sys.argv[2]), "candidate_id"])
PY
)
work="$PROJECT_DIR/performance_artifacts.round1/raw_orca/$candidate_id"
mkdir -p "$work"
cp "$PROJECT_DIR/performance_artifacts.round1/orca_inputs/$candidate_id.inp" "$work/candidate.inp"
cd "$work"
{ module list 2>&1; orca --version; } | tee environment.round1.log
orca candidate.inp > candidate.out
