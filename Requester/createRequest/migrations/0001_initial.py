# Generated by Django 3.0.7 on 2022-02-19 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('hospital', models.CharField(max_length=100)),
                ('blood_type', models.CharField(max_length=10)),
                ('urgency', models.CharField(max_length=10)),
                ('prescription_link', models.CharField(max_length=100)),
                ('pub_date', models.DateField(verbose_name='Date of Request')),
            ],
        ),
    ]
