# Generated by Django 4.1.1 on 2022-10-06 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_topic_rooms_host_message_rooms_topic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
