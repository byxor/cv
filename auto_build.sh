#!/bin/bash

echo "Setting up automatic recompilation of CV..."
echo
echo "If new python files are created, please re-run this command."
echo "Leave this running in a terminal somewhere."
echo "----------------------------------------------"

echo "Serving directory..."
live-server &

echo "Enabling auto-recompile..."
find . -name '*.py' ! -path '*/venv/*' | entr -p "./build_cv.sh"
