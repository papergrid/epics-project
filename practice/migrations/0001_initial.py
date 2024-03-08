# Generated by Django 5.0.1 on 2024-02-08 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('rollnumber', models.IntegerField(primary_key=True, serialize=False)),
                ('registration_no', models.IntegerField(max_length=20)),
                ('student_name', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('semester', models.IntegerField()),
                ('mobile_number', models.CharField(max_length=15)),
                ('email_id', models.EmailField(max_length=100)),
            ],
        ),
    ]