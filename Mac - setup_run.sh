#!/bin/bash

echo "============================"
echo "Cloning LMS project..."
echo "============================"

git clone https://github.com/getb10010/LMS-attendance.git

cd LMS-attendance

echo ""
echo "============================"
echo "Installing requirements..."
echo "============================"

pip3 install -r requirements.txt

echo ""
echo "============================"
echo "Starting project..."
echo "============================"

python3 main.py