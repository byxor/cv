#!/bin/bash

echo "Setting up automatic recompilation of CV..."
echo "* Leave this running in a terminal somewhere."
echo "* If new python files are created, please re-run this command."
find . -name '*.py' ! -path '*/venv/*' | entr -p "./build_cv.sh"
