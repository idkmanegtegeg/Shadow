@echo off
echo Setting up the environment...

:: Try using 'python'
where python >nul 2>&1
if %errorlevel%==0 (
    set PYTHON_CMD=python
) else (
    :: If 'python' isn't found, try 'py'
    where py >nul 2>&1
    if %errorlevel%==0 (
        set PYTHON_CMD=py
    ) else (
        echo Python is not installed. Please install Python and try again.
        pause
        exit /b
    )
)

:: Install pip if not installed
%PYTHON_CMD% -m ensurepip --upgrade

:: Upgrade pip
%PYTHON_CMD% -m pip install --upgrade pip

:: Install requirements
%PYTHON_CMD% -m pip install -r requirements.txt

echo Setup complete.
pause
