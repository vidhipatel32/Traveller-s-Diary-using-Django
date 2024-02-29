# Generated by Django 4.2.4 on 2023-09-28 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('season', models.CharField(max_length=20)),
                ('duration', models.IntegerField()),
                ('price', models.IntegerField()),
                ('description', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='dest/images/')),
            ],
        ),
    ]
