# Generated by Django 3.0.8 on 2021-06-14 18:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productrekmends', '0006_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='catname',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='productrekmends.categories'),
        ),
    ]
