# Generated by Django 2.2 on 2021-01-15 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='one_click_purchasing',
            field=models.BooleanField(default=False),
        ),
    ]
