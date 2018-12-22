#!/bin/bash

set -e
trap 'shout "Something went wrong, sorry."' exit

shouts=0
function shout {
    local banner="----------------------------------------"
    echo
    echo $banner
    echo "MESSAGE ${shouts}: $1"
    echo $banner
    echo
    shouts=$((shouts + 1))
}

clear

shout "Python -> LaTeX..."
python main.py

shout "LaTeX -> PDF..."
pdflatex cv.tex < /dev/null

shout "Displaying PDF..."
firefox cv.pdf

shout "Done!"
