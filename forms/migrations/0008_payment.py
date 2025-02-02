# Generated by Django 5.1 on 2024-08-27 14:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0007_course_timetable'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('payment_status', models.CharField(choices=[('Pending', 'Kutilmoqda'), ('Completed', 'Tugallangan'), ('Failed', 'Xato')], default='Pending', max_length=20)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forms.student')),
            ],
            options={
                'verbose_name': "To'lov",
                'verbose_name_plural': "To'lovlar",
            },
        ),
    ]
