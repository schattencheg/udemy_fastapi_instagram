@echo off
taskkill /F /IM uvicorn.exe 2>nul
if %errorlevel% equ 0 (
    echo ✓ Stopped all uvicorn processes
) else (
    echo No uvicorn processes running
)


echo Stopping RabbitMQ and Redis services...
taskkill /f /im beam.smp.exe >nul 2>&1
taskkill /f /im redis-server.exe >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo Note: RabbitMQ/Redis may not have been running
)

echo Terminating Python processes...
taskkill /f /im python.exe
if %ERRORLEVEL% NEQ 0 (
    echo Note: No Python processes were running or insufficient privileges to terminate them
)

echo System stopped successfully!