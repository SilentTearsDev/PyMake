#!/usr/bin/env bash
set -euo pipefail

# Resolve the directory this script lives in, so it works
# no matter where it's called from.
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TARGET="$SCRIPT_DIR/PyMake.py"
BIN_DIR="$HOME/.local/bin"
LINK="$BIN_DIR/pymake"

if [ ! -f "$TARGET" ]; then
    echo "✗ Cannot find PyMake.py next to this script ($TARGET)."
    exit 1
fi

echo "Installing PyMake..."

chmod +x "$TARGET"
mkdir -p "$BIN_DIR"

if [ -e "$LINK" ] || [ -L "$LINK" ]; then
    echo "  Removing existing $LINK"
    rm -f "$LINK"
fi

ln -s "$TARGET" "$LINK"
echo "✓ Linked $LINK -> $TARGET"

case ":$PATH:" in
    *":$BIN_DIR:"*)
        echo "✓ $BIN_DIR is already on your PATH"
        ;;
    *)
        echo "⚠ $BIN_DIR is not on your PATH."
        echo "  Add this to your ~/.bashrc or ~/.zshrc:"
        echo "    export PATH=\"\$HOME/.local/bin:\$PATH\""
        ;;
esac

echo
echo "Done! Open a new terminal (or 'source' your shell rc file) and run: pymake"
