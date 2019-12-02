psql -c "drop database photography;" &&
psql -c "create database photography;" &&
rm main/migrations/* &&
touch main/migrations/__init__.py &&
./manage.py makemigrations &&
./manage.py migrate &&
./manage.py init
