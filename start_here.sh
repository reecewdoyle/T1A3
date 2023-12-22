#!/bin/bash

if [[ -x "$(command -v python)" ]]; then
    pyv="$(python -V 2>&1)"
    if [[ $pyv == "Python 3"* ]]; then
        echo "Python is installed. Version: $pyv"
    else
        echo "This app requires python 3. Get it here: https://www.python.org/downloads/"  >&2
    fi
else
    echo "This app requires python 3. Get it here: https://www.python.org/downloads/" >&2
fi

./run.sh