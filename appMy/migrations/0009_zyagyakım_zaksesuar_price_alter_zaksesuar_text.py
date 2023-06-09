# Generated by Django 4.1.5 on 2023-04-03 13:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0008_remove_zaksesuar_price_alter_zaksesuar_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZYagyakım',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Marka')),
                ('img', models.ImageField(upload_to='', verbose_name='Fotoğraf')),
                ('text', models.TextField(max_length=500000, verbose_name='Açıklama')),
            ],
        ),
        migrations.AddField(
            model_name='zaksesuar',
            name='price',
            field=models.FloatField(default=0, verbose_name='Fiyat'),
        ),
        migrations.AlterField(
            model_name='zaksesuar',
            name='text',
            field=models.TextField(max_length=500, verbose_name='Açıklama'),
        ),
    ]
