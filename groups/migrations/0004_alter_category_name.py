# Generated by Django 4.0.5 on 2022-10-08 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("groups", "0003_group_description_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(max_length=100, null=True),
        ),
    ]
