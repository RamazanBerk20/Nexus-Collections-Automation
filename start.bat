set arg1=%1

Scripts\activate.bat && python.exe -m pip install --upgrade pip && pip install -r requirements.txt && main.py %arg1%