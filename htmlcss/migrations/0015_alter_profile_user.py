# Generated by Django 4.0.4 on 2022-04-27 04:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('htmlcss', '0014_alter_profile_token_alter_profile_verify'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='htmlcss.member'),
        ),
    ]