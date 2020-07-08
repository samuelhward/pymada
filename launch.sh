#!/bin/env bash

#install step here or line below
export PYTHONPATH=pymada:$PYTHONPATH
pytest -s tests/piece.py
python -m pymada.launch

