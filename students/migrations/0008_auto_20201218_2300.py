# Generated by Django 3.1.4 on 2020-12-18 23:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_courses_weer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courses',
            old_name='weer',
            new_name='week',
        ),
    ]
