#!/bin/env bash

#install step here or line below
export PYTHONPATH=pymada:$PYTHONPATH
./run_tests.sh
python -m pymada.launch

