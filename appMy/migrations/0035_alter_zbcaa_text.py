# Generated by Django 4.1.5 on 2023-04-21 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0034_alter_zsoya_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zbcaa',
            name='text',
            field=models.TextField(max_length=5000, verbose_name='Açıklama'),
        ),
    ]
