@ECHO OFF
start cmd /c python ./BC.py
timeout /t 1
start cmd /c python ./BR.py
timeout /t 1
start cmd /c python ./C.py
timeout /t 1
start cmd /c python ./S.py