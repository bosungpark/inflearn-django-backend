# Generated by Django 3.2.8 on 2021-10-28 04:49

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inflearn_lecture', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mytext',
            name='board_text',
            field=ckeditor.fields.RichTextField(null=True),
        ),
    ]
