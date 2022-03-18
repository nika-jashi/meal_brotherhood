# Generated by Django 4.0.1 on 2022-03-18 11:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('poll', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('going_out_or_not', models.BooleanField(default=False)),
                ('image', models.ImageField(default='default_pic.png', upload_to='profile_pics')),
                ('res', models.ForeignKey(blank=True, max_length=30, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='poll.restaurantlist')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
