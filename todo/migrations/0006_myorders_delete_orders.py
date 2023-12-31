# Generated by Django 4.2.4 on 2023-08-29 10:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('todo', '0005_orders'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyOrders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordername', models.CharField(default='NA', max_length=35)),
                ('amount', models.IntegerField()),
                ('status', models.CharField(default='Failed', max_length=35)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Orders',
        ),
    ]
