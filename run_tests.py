#!/bin/bash

# activate the virtual environment
source ./venv/bin/activate

# run the test suite
python -m pytest test/test_pink_morsel_sale_visualizer.py

PYTEST_EXIT_CODE=$?

# return exit code 0 if all tests pass or 1 otherwise
if [ $PYTEST_EXIT_CODE -eq 0 ]
then
    exit 0
else
    exit 1
    fi