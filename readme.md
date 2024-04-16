# Install requirements.txt
```pip install -r requirements.txt
```
# Run django server
python manage.py runserver

Note : Make sure you have properly installed redis server or RabbitMQ and it is working properly.
Run celery worker:
celery -A project worker -l info -P eventlet

Note: "project" is the name of our project
Run celery beat:
celery -A project beat -l info

Now both celery worker and celery beat will work.
If any of these do not work properly then check your redis or RabbitMQ

The celery beat will run a task in every one minute. 
Task is to send email using AWS SMTP. So make sure to change SMTP credentials. Also change sender email in task.py file.