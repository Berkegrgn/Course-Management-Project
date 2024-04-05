# Generated by Django 5.0.2 on 2024-03-26 11:46

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0010_uploadmodel_remove_course_imageurl_course_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='subtitle',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
