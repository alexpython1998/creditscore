# Generated by Django 2.1.3 on 2019-02-08 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190208_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='choices',
            field=models.ManyToManyField(blank=True, null=True, to='accounts.Choice'),
        ),
    ]
