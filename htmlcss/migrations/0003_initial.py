# Generated by Django 4.0.4 on 2022-04-22 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('htmlcss', '0002_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=10)),
                ('funame', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
                ('mobile', models.IntegerField()),
                ('pass1', models.CharField(max_length=20)),
                ('pass2', models.CharField(max_length=20)),
            ],
        ),
    ]
