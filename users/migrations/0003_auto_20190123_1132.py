# Generated by Django 2.1.5 on 2019-01-23 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_relationship'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='電子郵件'),
        ),
    ]
