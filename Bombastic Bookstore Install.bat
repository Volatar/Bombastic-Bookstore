@echo on

REM 1. Create and activate the virtual environment
python -m venv Virtualenv
call Virtualenv\Scripts\activate

REM 2. Install dependencies
pip install -r requirements.txt

REM 3. Run the project
cd %~dp0
start "" cmd /c "flask run"

REM 4. Wait for Flask server to start
timeout /t 5

REM 5. Opens browser
start "" http://127.0.0.1:5000



