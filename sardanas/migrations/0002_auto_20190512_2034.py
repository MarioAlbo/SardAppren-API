# Generated by Django 2.2 on 2019-05-12 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sardanas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sardana',
            name='file',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
