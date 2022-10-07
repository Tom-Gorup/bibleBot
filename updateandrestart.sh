#!/bin/bash

git pull
pkill -f -9 main.py
nohup python3 main.py > output.file 2>&1 &