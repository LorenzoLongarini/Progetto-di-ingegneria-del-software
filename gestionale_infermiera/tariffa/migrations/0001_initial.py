# Generated by Django 4.0.4 on 2022-05-08 10:55

from django.db import migrations, models
import tariffa.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tariffa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(help_text='Nome', max_length=10, verbose_name='Nome')),
                ('descrizione', models.TextField(blank=True, default=None, help_text='Descrizione', max_length=30, null=True, verbose_name='Descrizione')),
                ('prezzo', models.FloatField(help_text='Prezzo', max_length=6, validators=[tariffa.models.validate_price], verbose_name='Prezzo')),
            ],
        ),
    ]
