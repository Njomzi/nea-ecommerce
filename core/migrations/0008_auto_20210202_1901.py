# Generated by Django 2.2 on 2021-02-02 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_auto_20210130_2152'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name_plural': 'Adresat'},
        ),
        migrations.AlterField(
            model_name='address',
            name='address_type',
            field=models.CharField(choices=[('Fa', 'Faturimi'), ('T', 'Transporti')], max_length=1),
        ),
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('P', 'primare'), ('S', 'sekondare'), ('Rr', 'e rrezikshme')], max_length=1),
        ),
    ]
