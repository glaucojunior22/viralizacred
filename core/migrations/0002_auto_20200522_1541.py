# Generated by Django 3.0.6 on 2020-05-22 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parcela',
            name='banco',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='parcela',
            name='tipo',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
