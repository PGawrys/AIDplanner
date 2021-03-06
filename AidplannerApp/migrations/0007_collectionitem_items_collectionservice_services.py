# Generated by Django 4.0.3 on 2022-04-08 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AidplannerApp', '0006_remove_collectionitem_items_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='collectionitem',
            name='items',
            field=models.ManyToManyField(to='AidplannerApp.item'),
        ),
        migrations.AddField(
            model_name='collectionservice',
            name='services',
            field=models.ManyToManyField(to='AidplannerApp.service'),
        ),
    ]
