# Generated by Django 3.2.9 on 2022-01-07 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_discussionroom_roomparticipants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussionroom',
            name='roomName',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
