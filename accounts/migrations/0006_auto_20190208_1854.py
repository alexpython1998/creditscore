# Generated by Django 2.1.3 on 2019-02-08 18:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_userpolls'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpolls',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
