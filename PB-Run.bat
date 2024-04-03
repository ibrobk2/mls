@echo off
title Running Flask App

REM Activate Python environment if necessary
REM Replace 'path\to\your\python\env\Scripts\activate' with the path to your Python environment activation script
REM Uncomment the following line if you need to activate a virtual environment
REM call path\to\your\python\env\Scripts\activate

REM Run the Flask app
start cmd /k python app.py

REM Open default browser
start "" "http://localhost:5000"

echo Running Flask app. Press any key to stop the server and exit...
pause >nul

REM Stop the Flask server
taskkill /f /im python.exe /t >nul

exit
