# Generated by Django 3.2.5 on 2021-11-15 03:23

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0020_alter_question_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='body',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
