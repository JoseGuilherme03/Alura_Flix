sudo apt-get install -y libmysqlclient-dev
release: bash setup.sh && python manage.py migrate && python manage.py collectstatic --noinput
