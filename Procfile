release: python manage.py makemigrations catalog && python manage.py migrate catalog --no-input && python manage.py makemigrations && python manage.py migrate --no-input

web: gunicorn locallibrary.wsgi --log-file -
