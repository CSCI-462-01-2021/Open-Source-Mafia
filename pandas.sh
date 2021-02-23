#!/bin/bash

# sudo apt install git python-minimal python-all-dev python3-venv 

echo "Enter your GitHub username:"
read github

# echo $github

git clone https://github.com/$github/pandas-dev Desktop/pandas-$github

cd pandas-$github 

python3 -m venv ~/virtualenvs/pandas-dev
. ~/virtualenvs/pandas-dev
python -m pip install -r requirements-dev.txt

python setup.py build_ext -j 4
python -m pip install -e . --no-build-isolation --no-use-pep517

git checkout -b style