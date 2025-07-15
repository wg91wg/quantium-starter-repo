#!/bin/bash

python3 -m venv venv

source venv/bin/activate

pip install --upgrade pip

pip install "dash[testing]" pytest

pytest test_app.py

pytest test_app.py

if [ $? -eq 0 ]; then
  exit 0
else
  exit 1
fi