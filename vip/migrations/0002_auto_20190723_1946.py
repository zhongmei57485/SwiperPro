# Generated by Django 2.2.1 on 2019-07-23 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vip', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vippermission',
            old_name='vip_idd',
            new_name='vip_id',
        ),
        migrations.AlterField(
            model_name='permission',
            name='name',
            field=models.CharField(max_length=32, unique=True),
        ),
        migrations.AlterField(
            model_name='vip',
            name='level',
            field=models.IntegerField(default=0, unique=True),
        ),
        migrations.AlterField(
            model_name='vip',
            name='name',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
