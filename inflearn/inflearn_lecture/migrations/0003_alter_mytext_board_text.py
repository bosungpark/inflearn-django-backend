# Generated by Django 3.2.8 on 2021-10-28 04:54

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inflearn_lecture', '0002_mytext_board_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mytext',
            name='board_text',
            field=ckeditor_uploader.fields.RichTextUploadingField(null=True),
        ),
    ]
