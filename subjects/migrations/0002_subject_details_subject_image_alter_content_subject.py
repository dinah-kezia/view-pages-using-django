# Generated by Django 5.1.3 on 2024-11-07 07:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("subjects", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="subject",
            name="details",
            field=models.TextField(default="No content available"),
        ),
        migrations.AddField(
            model_name="subject",
            name="image",
            field=models.ImageField(
                default="No content available", upload_to="subject_images/"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="content",
            name="subject",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="contents",
                to="subjects.subject",
            ),
        ),
    ]
