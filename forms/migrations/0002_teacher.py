# Generated by Django 5.1 on 2024-08-27 09:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=13)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.school')),
            ],
            options={
                'verbose_name': "O'qituvchi",
                'verbose_name_plural': "O'qituvchilar",
            },
        ),
    ]
