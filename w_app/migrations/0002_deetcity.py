# Generated by Django 2.2 on 2020-04-25 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('w_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeetCity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deetname', models.CharField(max_length=25)),
            ],
            options={
                'verbose_name_plural': 'cities',
            },
        ),
    ]
