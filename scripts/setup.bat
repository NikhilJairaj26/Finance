@echo off

echo =====================================
echo      FINANCE APP SETUP SCRIPT
echo =====================================

:: 1. Create Conda environment
echo [1/4] Creating Conda environment...
conda create --prefix ../finance_env python=3.9 -y

:: 2. Activate Conda environment
call conda activate ../finance_env

:: 3. Install backend dependencies
echo [2/4] Installing backend dependencies...
cd ../backend
pip install -r requirements.txt
cd ../scripts

:: 4. Install frontend dependencies
echo [3/4] Installing frontend dependencies...
cd ../mobile
npm install
cd ../scripts

:: 5. Initialize React Native project (if not already)
:: This step is manual for now. Run `npx react-native init mobile` if you haven't.

echo [4/4] Setup complete!
pause
