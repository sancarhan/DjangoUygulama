# Generated by Django 4.1.5 on 2023-04-05 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0020_zwhey_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='zbcaa',
            name='list',
            field=models.TextField(blank=True, max_length=5000, verbose_name='Liste'),
        ),
        migrations.AddField(
            model_name='zcasein',
            name='list',
            field=models.TextField(blank=True, max_length=5000, verbose_name='Liste'),
        ),
        migrations.AddField(
            model_name='zcreatin',
            name='list',
            field=models.TextField(blank=True, max_length=5000, verbose_name='Liste'),
        ),
        migrations.AddField(
            model_name='zsoya',
            name='list',
            field=models.TextField(blank=True, max_length=5000, verbose_name='Liste'),
        ),
    ]
