import os


print("Desplegando Django...")
os.system("pip install -r requirements.txt")
os.system("python manage.py makemigrations")
os.system("python manage.py collectstatic")
os.system("python manage.py migrate")
os.system("python manage.py runserver")
