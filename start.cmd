@echo off
echo Starting Uvicorn server...
uvicorn main:app --reload
pause