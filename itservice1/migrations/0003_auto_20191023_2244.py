# Generated by Django 2.2.6 on 2019-10-23 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itservice1', '0002_entry'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='title',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='topic',
            name='text',
            field=models.CharField(max_length=20),
        ),
    ]
