# Generated by Django 3.1 on 2021-01-14 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210114_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='Profile_Photo',
            field=models.ImageField(blank=True, default='home/default.png', null=True, upload_to='static/home'),
        ),
    ]
