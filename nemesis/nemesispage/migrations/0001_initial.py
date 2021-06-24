# Generated by Django 3.2.4 on 2021-06-23 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userlogin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lname', models.CharField(max_length=42)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=250)),
                ('ladd', models.CharField(max_length=50)),
            ],
        ),
    ]