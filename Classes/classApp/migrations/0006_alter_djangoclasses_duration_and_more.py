# Generated by Django 4.0 on 2021-12-16 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classApp', '0005_alter_djangoclasses_course_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='djangoclasses',
            name='duration',
            field=models.DurationField(choices=[(30, 30), (60, 60), (90, 90)]),
        ),
        migrations.AlterField(
            model_name='djangoclasses',
            name='instructor',
            field=models.CharField(choices=[('M.Hatter', 'M.Hatter'), ('A.Jones', 'A.Jones'), ('K.Bryant', 'K.Bryant')], max_length=30),
        ),
        migrations.AlterField(
            model_name='djangoclasses',
            name='title',
            field=models.CharField(choices=[('Django 102', 'Django 102'), ('Django 103', 'Django 103'), ('Django 101', 'Django 101')], max_length=30),
        ),
    ]
