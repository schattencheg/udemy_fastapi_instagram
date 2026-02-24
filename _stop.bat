@echo off
taskkill /F /IM uvicorn.exe 2>nul
if %errorlevel% equ 0 (
    echo ✓ Stopped all uvicorn processes
) else (
    echo No uvicorn processes running
)
