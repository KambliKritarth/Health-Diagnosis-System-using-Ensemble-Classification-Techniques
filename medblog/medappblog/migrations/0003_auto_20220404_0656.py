# Generated by Django 3.2.5 on 2022-04-04 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medappblog', '0002_hdsymptom'),
    ]

    operations = [
        migrations.AddField(
            model_name='hdsymptom',
            name='CreatiPhosph',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hdsymptom',
            name='EjectFract',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hdsymptom',
            name='SerCreat',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hdsymptom',
            name='SerSodiu',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hdsymptom',
            name='age',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hdsymptom',
            name='anaemia',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='hdsymptom',
            name='followUpTime',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hdsymptom',
            name='highBP',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='hdsymptom',
            name='sex',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='hdsymptom',
            name='smoking',
            field=models.CharField(default='', max_length=255),
        ),
    ]
