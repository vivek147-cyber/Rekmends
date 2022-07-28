# Generated by Django 3.2.5 on 2021-08-22 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productrekmends', '0013_auto_20210701_1215'),
    ]

    operations = [
        migrations.CreateModel(
            name='deals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('discount', models.CharField(blank=True, default='', max_length=50)),
                ('image', models.ImageField(default='', upload_to='attachments/')),
                ('link', models.URLField(default='', max_length=500)),
                ('price', models.IntegerField()),
            ],
        ),
    ]