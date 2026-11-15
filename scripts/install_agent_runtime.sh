#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PROFILE="${1:-core}"
ENV_DIR="${2:-$ROOT/.venvs/agent-runtime-$PROFILE}"
case "$PROFILE" in
  core) REQUIREMENTS="$ROOT/requirements-agent-runtime-core.txt" ;;
  adk) REQUIREMENTS="$ROOT/requirements-agent-runtime-adk.txt" ;;
  microsoft) REQUIREMENTS="$ROOT/requirements-agent-runtime-microsoft.txt" ;;
  agno) REQUIREMENTS="$ROOT/requirements-agent-runtime-agno.txt" ;;
  crewai) echo "BLOCKED: CrewAI package layout is experimental and not installable from this profile."; exit 2 ;;
  *) echo "Usage: $0 {core|adk|microsoft|agno} [venv-path]"; exit 2 ;;
esac
if [[ -e "$ENV_DIR" ]]; then
  echo "BLOCKED: environment already exists: $ENV_DIR"
  echo "Use a new versioned path to preserve reproducibility."
  exit 3
fi
python3 -m venv "$ENV_DIR"
"$ENV_DIR/bin/python" -m pip install --upgrade pip
"$ENV_DIR/bin/python" -m pip install --requirement "$REQUIREMENTS"
"$ENV_DIR/bin/python" -m pip freeze > "$ENV_DIR/requirements.resolved.txt"
echo "INSTALL_COMPLETE profile=$PROFILE env=$ENV_DIR"
echo "NOTE: installation is not runtime verification; execute acceptance tests separately."
