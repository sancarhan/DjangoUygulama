# Generated by Django 4.1.5 on 2023-04-02 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appMy', '0005_soya'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Soya',
            new_name='ZCasein',
        ),
        migrations.RenameModel(
            old_name='Casein',
            new_name='ZSoya',
        ),
        migrations.RenameModel(
            old_name='whey',
            new_name='ZWhey',
        ),
    ]
