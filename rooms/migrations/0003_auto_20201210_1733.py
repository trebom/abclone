# Generated by Django 2.2.5 on 2020-12-10 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_auto_20201210_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='room_type',
            field=models.ManyToManyField(blank=True, null=True, related_name='rooms', to='rooms.RoomType'),
        ),
    ]
