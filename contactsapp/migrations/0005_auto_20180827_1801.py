# Generated by Django 2.1 on 2018-08-27 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactsapp', '0004_auto_20180827_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='image',
            field=models.ImageField(blank=True, upload_to='contact_avatars/', verbose_name='Логотип офиса'),
        ),
    ]
