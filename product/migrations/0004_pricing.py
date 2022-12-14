# Generated by Django 4.0.6 on 2022-08-09 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_categories'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(null=True)),
                ('full_support', models.CharField(max_length=10)),
                ('duration', models.IntegerField(default=0)),
                ('storage', models.IntegerField(default=0)),
                ('price', models.IntegerField(default=0)),
            ],
        ),
    ]
