# Generated by Django 4.2.4 on 2023-08-23 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('mobile_no', models.CharField(max_length=11)),
                ('father_name', models.CharField(max_length=100)),
                ('passport_no', models.IntegerField()),
            ],
        ),
    ]
