from django.db import models

#create table todo(
#id serial primary key, #id django auto haldinxa
#title varchar(255)
#)

# if there is any change in models.py, run following:
# python manage.py makemigrations
#python manage.py migrate

class Todo(models.Model):
    title = models.CharField(max_length=200)
# completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title