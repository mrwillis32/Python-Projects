

from django.db import models


# created our objects

# Create your models here.


class DjangoClasses(models.Model):
    title = models.CharField(max_length=30)
    course_number = models.IntegerField(max_length=200)
    instructor = models.CharField(max_length=30)
    duration = models.DurationField()


DjangoClasses.objects.create(title='SE 101', course_number=100, instructor='K.Bryant', duration=30.0)
objects = models.Manager()


def __str__(self):
    return self.name
