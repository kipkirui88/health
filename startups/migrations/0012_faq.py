# Generated by Django 3.0.6 on 2023-01-22 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startups', '0011_auto_20230121_2155'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
    ]