# Generated by Django 4.1.1 on 2022-09-15 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predict', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image_entry',
            field=models.ImageField(upload_to='cricketImages'),
        ),
    ]
