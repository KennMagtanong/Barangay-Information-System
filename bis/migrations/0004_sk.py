# Generated by Django 4.0.1 on 2022-01-19 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bis', '0003_blotter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=30)),
                ('position', models.CharField(max_length=30)),
            ],
        ),
    ]
