# Generated by Django 4.1.7 on 2023-03-20 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ssapp', '0002_details_alter_course_name_alter_department_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='name',
            new_name='course',
        ),
        migrations.RenameField(
            model_name='department',
            old_name='name',
            new_name='department',
        ),
    ]