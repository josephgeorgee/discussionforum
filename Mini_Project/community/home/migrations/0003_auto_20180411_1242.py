# Generated by Django 2.0.2 on 2018-04-11 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20180407_1742'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='occupatipon',
            new_name='occupation',
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]