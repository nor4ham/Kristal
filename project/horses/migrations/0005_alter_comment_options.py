# Generated by Django 4.0.4 on 2022-06-14 09:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('horses', '0004_profilehorse_price'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-comment_daate']},
        ),
    ]
