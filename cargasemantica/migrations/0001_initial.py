# Generated by Django 4.0.3 on 2022-03-25 12:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Metadatos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aliasconxion', models.CharField(max_length=30)),
                ('comentariobd', models.TextField(max_length=150)),
                ('nomhost', models.CharField(max_length=10)),
                ('nompuerto', models.IntegerField()),
                ('nombd', models.CharField(max_length=20)),
                ('usuario', models.CharField(max_length=30)),
                ('passw', models.CharField(max_length=25)),
                ('fechacreacion', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
