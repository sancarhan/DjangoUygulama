# Generated by Django 4.1.5 on 2023-04-03 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0007_zaksesuar_zaminoasit_zbcaa_zcreatin_zkafein_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='zaksesuar',
            name='price',
        ),
        migrations.AlterField(
            model_name='zaksesuar',
            name='text',
            field=models.TextField(max_length=500000, verbose_name='Açıklama'),
        ),
    ]
