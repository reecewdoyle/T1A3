#!/bin/bash

python3 -m venv .venv
source .venv/bin/activate
pip3 install colored
pip3 install DateTime
pip3 install prettytable
pip3 install pyfiglet
pip3 install pytz
pip3 install wcwidth
pip3 install zope.interface
python3 main.py
