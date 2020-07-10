#!/bin/env bash

#install step here or line below
export PYTHONPATH=pymada:$PYTHONPATH
pytest -s tests/piece.py
pytest -s tests/ship.py
pytest -s tests/position.py
python -m pymada.launch

