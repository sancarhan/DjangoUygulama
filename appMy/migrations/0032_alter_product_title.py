# Generated by Django 4.1.5 on 2023-04-19 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0031_alter_category_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Başlık'),
        ),
    ]
