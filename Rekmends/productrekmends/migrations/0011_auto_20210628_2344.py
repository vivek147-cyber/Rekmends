# Generated by Django 3.0.8 on 2021-06-28 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productrekmends', '0010_product_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
