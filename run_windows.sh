python -m venv .env
source .env/Scripts/activate
pip install -r requirements.txt
cd src/
python manage.py makemigrations
python manage.py makemigrations accounts
python manage.py migrate
python manage.py runserver