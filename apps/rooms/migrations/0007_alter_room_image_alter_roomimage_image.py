# Generated by Django 4.2 on 2025-07-19 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0006_room_description_ru_room_description_uz_room_name_ru_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media_zone/rooms/'),
        ),
        migrations.AlterField(
            model_name='roomimage',
            name='image',
            field=models.ImageField(upload_to='media_zone/room_images/'),
        ),
    ]
