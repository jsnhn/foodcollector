# Generated by Django 5.0.6 on 2024-06-06 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cuisine', models.CharField(max_length=100)),
                ('review', models.TextField(max_length=250)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('vegitarian', models.BooleanField(default=False)),
            ],
        ),
    ]
