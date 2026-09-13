#!/usr/bin/env bash
set -euo pipefail

BIN_DIR="$HOME/.local/bin"
LINK="$BIN_DIR/pymake"

echo "Uninstalling PyMake..."

if [ -L "$LINK" ] || [ -e "$LINK" ]; then
    rm -f "$LINK"
    echo "✓ Removed $LINK"
else
    echo "✓ Nothing to remove ($LINK does not exist)"
fi

echo
echo "Note: any .venv, requirements.txt, or main.py files created by"
echo "pymake in your projects are NOT touched by this script."
echo "You can safely delete the PyMake project folder now if you want."
