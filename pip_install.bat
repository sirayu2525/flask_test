@echo off
REM This is a case of no arguments being provided. Indicate how to use it.
if "%1"=="" (
    echo Usage: pip_install.bat package_name
    exit /b 1
)
pip install %*
pip freeze > requirements.txt
