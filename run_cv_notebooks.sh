#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
VENV="$ROOT_DIR/.venv"
NOTEBOOK_DIR="$ROOT_DIR/06_Computer_Vision_NLP"
OUTPUT_DIR="$NOTEBOOK_DIR/executed"

# Prefer project venv if present
if [ -d "$VENV" ]; then
  # shellcheck disable=SC1090
  source "$VENV/bin/activate"
fi

mkdir -p "$OUTPUT_DIR"

NOTEBOOKS=(
  "06_01_CNN_Grundlagen.ipynb"
  "06_02_Computer_Vision_Anwendungen.ipynb"
  "06_03_Data_Augmentation.ipynb"
  "06_04_Transfer_Learning.ipynb"
  "06_05_neu_Image_Sampler.ipynb"
)

failures=0
for nb in "${NOTEBOOKS[@]}"; do
  in_path="$NOTEBOOK_DIR/$nb"
  out_name="${nb%.ipynb}-executed.ipynb"
  tmp_nb="$(mktemp)"
  echo "=== Executing $nb ==="
  # Remove legacy cell ids to satisfy nbformat validators in older nbconvert versions.
  python - "$in_path" "$tmp_nb" <<'PY'
import json, pathlib, sys
src = pathlib.Path(sys.argv[1])
dst = pathlib.Path(sys.argv[2])
data = json.loads(src.read_text())
for cell in data.get("cells", []):
    cell.pop("id", None)
    meta = cell.get("metadata")
    if isinstance(meta, dict):
        meta.pop("id", None)
data.setdefault("metadata", {}).pop("id", None)
dst.write_text(json.dumps(data))
PY
  if jupyter nbconvert \
    --to notebook \
    --execute "$tmp_nb" \
    --output "$out_name" \
    --output-dir "$OUTPUT_DIR" \
    --ExecutePreprocessor.kernel_name=python3 \
    --ExecutePreprocessor.timeout=3600; then
    echo "[ok] $nb"
  else
    echo "[fail] $nb" >&2
    failures=$((failures + 1))
  fi
  rm -f "$tmp_nb"
  echo
done

if [ "$failures" -gt 0 ]; then
  echo "Notebook executions finished with $failures failure(s)." >&2
  exit 1
fi

echo "All notebooks executed successfully. Outputs in $OUTPUT_DIR"