# Generated by Django 4.2.7 on 2024-01-19 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('founded_year', models.PositiveIntegerField()),
                ('headquarters', models.CharField(max_length=255)),
                ('website', models.URLField()),
            ],
        ),
    ]
