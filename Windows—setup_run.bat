@echo off

echo ============================
echo Cloning LMS project...
echo ============================

git clone https://github.com/getb10010/LMS-attendance.git

cd LMS-attendance

echo.
echo ============================
echo Installing requirements...
echo ============================

pip install -r requirements.txt

echo.
echo ============================
echo Starting project...
echo ============================

python main.py

pause