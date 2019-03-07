#!/bin/csh

mkdir -p Train/lines
mkdir -p Train/curves
mkdir -p Test/lines
mkdir -p Test/curves

python generate_curves.py
python generate_lines.py
