# Generated by Django 4.0.3 on 2022-03-31 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AidplannerApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('services', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AidplannerApp.service')),
                ('spot', models.ManyToManyField(to='AidplannerApp.spot')),
            ],
        ),
        migrations.CreateModel(
            name='ItemList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AidplannerApp.item')),
                ('spot', models.ManyToManyField(to='AidplannerApp.spot')),
            ],
        ),
    ]
