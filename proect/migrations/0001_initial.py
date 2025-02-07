# Generated by Django 5.0.6 on 2024-06-26 17:46

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Klass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=150)),
                ('narxi', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Mehmonxona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=150)),
                ('yulduzlar_soni', models.DecimalField(decimal_places=2, max_digits=3, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('narxi', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Travel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=150)),
                ('izoh', models.TextField()),
                ('muddati', models.DateField()),
                ('narxi', models.PositiveIntegerField()),
                ('klass', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proect.klass')),
                ('mexmonxona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proect.mehmonxona')),
            ],
        ),
    ]
