# Generated by Django 4.0.4 on 2022-04-22 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('htmlcss', '0004_alter_user_funame_alter_user_id_alter_user_table'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Member',
        ),
    ]