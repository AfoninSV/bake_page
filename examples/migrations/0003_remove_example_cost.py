# Generated by Django 3.1.5 on 2021-10-31 20:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('examples', '0002_auto_20210209_1842'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='example',
            name='cost',
        ),
    ]