# Generated by Django 4.1.5 on 2023-04-03 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0010_alter_zyagyakım_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='ZFull',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Başlık')),
                ('img', models.ImageField(upload_to='', verbose_name='Fotoğraf')),
                ('text', models.TextField(max_length=500000, verbose_name='Açıklama')),
            ],
        ),
        migrations.CreateModel(
            name='ZGuc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Başlık')),
                ('img', models.ImageField(upload_to='', verbose_name='Fotoğraf')),
                ('text', models.TextField(max_length=500000, verbose_name='Açıklama')),
            ],
        ),
        migrations.CreateModel(
            name='ZGun',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Başlık')),
                ('img', models.ImageField(upload_to='', verbose_name='Fotoğraf')),
                ('text', models.TextField(max_length=500000, verbose_name='Açıklama')),
            ],
        ),
        migrations.CreateModel(
            name='ZHıt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Başlık')),
                ('img', models.ImageField(upload_to='', verbose_name='Fotoğraf')),
                ('text', models.TextField(max_length=500000, verbose_name='Açıklama')),
            ],
        ),
        migrations.CreateModel(
            name='ZIlerı',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Başlık')),
                ('img', models.ImageField(upload_to='', verbose_name='Fotoğraf')),
                ('text', models.TextField(max_length=500000, verbose_name='Açıklama')),
            ],
        ),
        migrations.CreateModel(
            name='ZMakro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Başlık')),
                ('img', models.ImageField(upload_to='', verbose_name='Fotoğraf')),
                ('text', models.TextField(max_length=500000, verbose_name='Açıklama')),
            ],
        ),
        migrations.CreateModel(
            name='ZNasıl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Başlık')),
                ('img', models.ImageField(upload_to='', verbose_name='Fotoğraf')),
                ('text', models.TextField(max_length=500000, verbose_name='Açıklama')),
            ],
        ),
        migrations.CreateModel(
            name='ZPpl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Başlık')),
                ('img', models.ImageField(upload_to='', verbose_name='Fotoğraf')),
                ('text', models.TextField(max_length=500000, verbose_name='Açıklama')),
            ],
        ),
        migrations.CreateModel(
            name='ZSecım',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Başlık')),
                ('img', models.ImageField(upload_to='', verbose_name='Fotoğraf')),
                ('text', models.TextField(max_length=500000, verbose_name='Açıklama')),
            ],
        ),
    ]
