# Generated by Django 4.0.5 on 2022-10-06 14:21

from django.db import migrations, models
import groups.models


class Migration(migrations.Migration):

    dependencies = [
        ("groups", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="group",
            name="image",
            field=models.ImageField(
                null=True, upload_to=groups.models.product_upload_path
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="age",
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name="student",
            name="email",
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name="student",
            name="name",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name="teacher",
            name="age",
            field=models.PositiveIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name="teacher",
            name="email",
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name="teacher",
            name="name",
            field=models.CharField(max_length=100, null=True),
        ),
    ]
