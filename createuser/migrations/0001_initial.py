# Generated by Django 4.0.3 on 2022-03-14 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Adduser',
            fields=[
                ('username', models.CharField(max_length=300, primary_key=True, serialize=False)),
                ('Password', models.CharField(max_length=100)),
                ('Fname', models.CharField(max_length=50)),
                ('Lname', models.CharField(max_length=50)),
                ('Address', models.CharField(max_length=50)),
                ('Phone_No', models.CharField(max_length=10)),
                ('Email', models.CharField(max_length=100)),
            ],
        ),
    ]
