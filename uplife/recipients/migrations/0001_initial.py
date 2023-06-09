# Generated by Django 3.2.19 on 2023-05-08 08:20

from django.db import migrations, models
import localflavor.br.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BagType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='nome')),
                ('specification', models.CharField(max_length=50, null=True, verbose_name='especificação')),
                ('capacity', models.PositiveIntegerField(verbose_name='capacidade')),
            ],
            options={
                'verbose_name': 'tipo de bolsa',
                'verbose_name_plural': 'tipos de bolsas',
            },
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cnpj', localflavor.br.models.BRCNPJField(max_length=18, unique=True, verbose_name='CNPJ')),
                ('corporate_name', models.CharField(max_length=60, verbose_name='razão social')),
                ('address', models.CharField(max_length=60, verbose_name='logradouro')),
                ('district', models.CharField(max_length=30, verbose_name='bairro')),
                ('city', models.CharField(max_length=30, verbose_name='cidade')),
                ('state', localflavor.br.models.BRStateField(max_length=2, verbose_name='estado')),
                ('zip_code', localflavor.br.models.BRPostalCodeField(max_length=9, unique=True, verbose_name='CEP')),
            ],
            options={
                'verbose_name': 'instituição',
                'verbose_name_plural': 'instituições',
            },
        ),
        migrations.CreateModel(
            name='MedicineType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trade_name', models.CharField(max_length=50, verbose_name='nome comercial')),
                ('generic_name', models.CharField(max_length=50, null=True, verbose_name='nome genérico')),
                ('risk_factor', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='fator de risco')),
            ],
            options={
                'verbose_name': 'tipo de medicamento',
                'verbose_name_plural': 'tipos de medicamentos',
            },
        ),
    ]
