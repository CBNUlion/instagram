# Generated by Django 2.1.7 on 2019-08-19 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0003_auto_20190819_2058'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-updated']},
        ),
    ]
