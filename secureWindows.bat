@echo off
rem Turn off command echoing to keep the output clean

rem Disable Windows Defender Real-time Protection by modifying the registry
REG ADD "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows Defender\Real-Time Protection" /v "DisableRealtimeMonitoring" /t REG_DWORD /d 1 /f

echo.
rem Display a message indicating that Windows Defender has been disabled
echo Windows Defender Real-time protection temporarily disabled.
pause
rem Wait for user input before closing the script
