# Generated by Django 4.0.4 on 2022-04-27 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('htmlcss', '0018_alter_profile_token_alter_profile_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='htmlcss.member'),
        ),
    ]