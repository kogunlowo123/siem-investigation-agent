#!/bin/bash
set -euo pipefail
echo "Setting up SIEM Investigation Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
