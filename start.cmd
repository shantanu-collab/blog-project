@echo off
echo Starting Uvicorn server...
python -m uvicorn main:app --reload
pause