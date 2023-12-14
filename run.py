import os


print("Desplegando Django...")
os.system("pip install -r requirements.txt")
os.system("python myproject/manage.py makemigrations")
os.system("python myproject/manage.py collectstatic")
os.system("python myproject/manage.py migrate")
os.system("python myproject/manage.py runserver")