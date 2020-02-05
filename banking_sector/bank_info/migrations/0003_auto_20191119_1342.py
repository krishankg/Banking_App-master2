# Generated by Django 2.2.7 on 2019-11-19 13:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bank_info', '0002_auto_20191119_1337'),
    ]

    operations = [
        migrations.RenameField(
            model_name='branchinfo',
            old_name='bank',
            new_name='bank_name',
        ),
        migrations.RemoveField(
            model_name='bankinfo',
            name='bank_id',
        ),
        migrations.AddField(
            model_name='branchinfo',
            name='bank_id',
            field=models.CharField(max_length=5),
            preserve_default=False,
        ),
    ]