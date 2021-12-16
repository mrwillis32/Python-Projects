from django.db import models

# created our objects
TITLE_CHOICES = {
    ('Django 101', 'Django 101'),
    ('Django 102','Django 102'),
    ('Django 103','Django 103'),
}

COURSE_NUMBER = {
    ('100','100'),
    ('102','102'),
    ('200','200'),
}

INSTRUCTOR_CHOICES = {
    ('K.Bryant','K.Bryant'),
    ('A.Jones','A.Jones'),
    ('M.Hatter','M.Hatter'),
}

DURATION_CHOICES = {
    (30,30),
    (60,60),
    (90,90),
}
# Create your models here.
class DjangoClasses(models.Model):
    title = models.CharField(max_length=30, choices=TITLE_CHOICES)
    course_number = models.IntegerField(choices=COURSE_NUMBER)
    instructor = models.CharField(max_length=30, choices=INSTRUCTOR_CHOICES)
    duration = models.DurationField(choices=DURATION_CHOICES)

    objects = models.Manager()

    def __str__(self):
        return self.name