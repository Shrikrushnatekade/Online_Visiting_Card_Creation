# Generated by Django 4.0.4 on 2022-04-21 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=20)),
                ('mobile', models.IntegerField()),
                ('password', models.CharField(max_length=20)),
                ('cpassword', models.CharField(max_length=20)),
            ],
        ),
    ]
