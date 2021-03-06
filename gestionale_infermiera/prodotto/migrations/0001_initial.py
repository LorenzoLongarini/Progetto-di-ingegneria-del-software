# Generated by Django 4.0.4 on 2022-05-07 14:07

import django.core.validators
from django.db import migrations, models
import prodotto.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Prodotto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=10)),
                ('descrizione', models.TextField(blank=True, help_text='Descrizione', null=True, verbose_name='Descrizione')),
                ('marca', models.CharField(blank=True, help_text='Marca', max_length=15, null=True, verbose_name='Marca')),
                ('prezzo', models.FloatField(help_text='Marca', max_length=3, validators=[prodotto.models.validate_price, django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999)], verbose_name='Marca')),
            ],
        ),
    ]
