# Generated by Django 5.1 on 2024-11-07 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("subjects", "0002_subject_details_subject_image_alter_content_subject"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subject",
            name="image",
            field=models.ImageField(upload_to="media/subject_images/"),
        ),
    ]