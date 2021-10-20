# Generated by Django 3.1.5 on 2021-01-30 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Example',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.FileField(blank=True, null=True, upload_to='')),
                ('cost', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
