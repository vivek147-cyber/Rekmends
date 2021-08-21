# Generated by Django 3.0.8 on 2021-07-01 06:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('productrekmends', '0012_coupon'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coupon',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]