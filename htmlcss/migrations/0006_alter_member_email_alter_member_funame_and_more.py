# Generated by Django 4.0.4 on 2022-04-22 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('htmlcss', '0005_rename_user_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='email',
            field=models.EmailField(max_length=200),
        ),
        migrations.AlterField(
            model_name='member',
            name='funame',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterModelTable(
            name='member',
            table=None,
        ),
    ]
