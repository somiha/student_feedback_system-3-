# Generated by Django 2.2.7 on 2021-07-04 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_reviewdetails_given'),
        ('account', '0005_auto_20210620_0321'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentprofile',
            name='retake',
            field=models.ManyToManyField(to='main.SemesterSubject'),
        ),
    ]