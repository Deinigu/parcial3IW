@echo off

:: Instalar los requisitos
pip install -r parcial3be\requirements.txt

:: Migrar la base de datos
python parcial3be\manage.py migrate

:: Iniciar backend en el puerto 8000
start cmd /k python parcial3be\manage.py runserver 8000

:: Instalar dependencias de node
cd parcial3fe\
npm install