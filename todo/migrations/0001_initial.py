# Generated by Django 4.2.4 on 2023-08-08 10:25

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
                ('sname', models.CharField(max_length=35)),
                ('marks', models.IntegerField()),
                ('doadmission', models.DateField()),
            ],
        ),
    ]
