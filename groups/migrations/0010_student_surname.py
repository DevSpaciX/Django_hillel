# Generated by Django 4.0.5 on 2022-10-14 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0009_remove_teacher_groups'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='surname',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]