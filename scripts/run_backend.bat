@echo off

echo =====================================
echo      RUNNING BACKEND SERVER
echo =====================================

call conda activate ./finance_env

cd backend
python run.py
