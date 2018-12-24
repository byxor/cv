#!/bin/bash

set -e
trap 'onError' ERR

function onError {
    shout "Something went wrong, sorry."
    notify-send "CV: Build Failed."
}

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

shout "Python -> LaTeX..."
python main.py

shout "LaTeX -> PDF..."
# pdflatex cv.tex < /dev/null
xelatex cv < /dev/null

# shout "Displaying PDF..."
# firefox cv.pdf

notify-send "CV: Build Successful."

shout "Done!"
