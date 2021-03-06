# Generated by Django 4.0.1 on 2022-03-21 06:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('poll', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('on_site', models.BooleanField(default=False)),
                ('who_orders', models.BooleanField(default=False)),
                ('image', models.ImageField(default='default_pic.png', upload_to='profile_pics')),
                ('menu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='poll.menu')),
                ('res', models.ForeignKey(blank=True, max_length=30, null=True, on_delete=django.db.models.deletion.SET_NULL, to='poll.restaurantlist')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
