@echo off
call venv\Scripts\activate.bat
pytest TestCases/test_login.py --html=Reports\report.html
