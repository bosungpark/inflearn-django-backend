# Generated by Django 3.2.8 on 2021-10-29 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inflearn_lecture', '0004_mytext_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mytext',
            name='img_url',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
