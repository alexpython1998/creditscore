# Generated by Django 2.1.3 on 2019-03-03 22:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_advice'),
    ]

    operations = [
        migrations.RenameField(
            model_name='advice',
            old_name='max_Score',
            new_name='max_score',
        ),
        migrations.RemoveField(
            model_name='advice',
            name='created',
        ),
    ]
