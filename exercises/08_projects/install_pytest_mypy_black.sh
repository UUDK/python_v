#!/bin/bash

# Install the packages `pytest`, `mypy`, and `black`

source venv/bin/activate
# .\venv\Scripts\activate.ps1

pip install pytest mypy black

pip freeze > requirements.txt
