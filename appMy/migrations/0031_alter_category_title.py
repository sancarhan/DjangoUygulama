# Generated by Django 4.1.5 on 2023-04-19 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0030_delete_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Kategori'),
        ),
    ]
