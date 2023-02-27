from django.db import models

class Student(models.Model):
    p_name = models.CharField(name='p_name', max_length=255)

