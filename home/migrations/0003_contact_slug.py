# Generated by Django 2.2.17 on 2021-01-16 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_contact_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='slug',
            field=models.CharField(default='', max_length=130),
            preserve_default=False,
        ),
    ]
