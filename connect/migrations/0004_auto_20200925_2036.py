# Generated by Django 3.1 on 2020-09-25 15:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('connect', '0003_remove_reunion_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reunion',
            name='Participants',
        ),
        migrations.RemoveField(
            model_name='reunion',
            name='user',
        ),
        migrations.DeleteModel(
            name='List',
        ),
        migrations.DeleteModel(
            name='Reunion',
        ),
    ]