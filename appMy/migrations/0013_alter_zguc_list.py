# Generated by Django 4.1.5 on 2023-04-04 22:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0012_zguc_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zguc',
            name='list',
            field=models.CharField(blank=True, max_length=5000, verbose_name='Liste'),
        ),
    ]
