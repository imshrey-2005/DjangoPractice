from django.db import models

# Create your models here.
class Task(models.Model):
    t_name=models.CharField(name='task',max_length=100)
    status=models.BooleanField(name='status',default=False)
    deadline=models.DateField(name='deadline')
