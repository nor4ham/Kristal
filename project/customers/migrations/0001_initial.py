# Generated by Django 4.0.4 on 2022-06-12 06:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileCustomer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('addres', models.CharField(blank=True, max_length=50, null=True)),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='photos/%y/%m/%d')),
                ('interests', models.CharField(blank=True, choices=[('Keheilan', 'Keheilan'), ('Seglawi', 'Seglawi'), ('Abeyan ', 'Abeyan '), ('Hamdani', 'Hamdani'), ('Hadban', 'Hadban')], max_length=200, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
