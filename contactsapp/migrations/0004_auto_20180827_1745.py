# Generated by Django 2.1 on 2018-08-27 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactsapp', '0003_contacts_avatar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacts',
            name='avatar',
        ),
        migrations.AddField(
            model_name='contacts',
            name='image',
            field=models.ImageField(blank=True, upload_to='contact_avatars', verbose_name='Логотип офиса'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='email',
            field=models.CharField(max_length=32, unique=True, verbose_name='E-mail'),
        ),
    ]