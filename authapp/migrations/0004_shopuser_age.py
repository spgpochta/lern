# Generated by Django 2.0.5 on 2018-08-03 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0003_remove_shopuser_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopuser',
            name='age',
            field=models.PositiveIntegerField(default=0, verbose_name='возраст'),
        ),
    ]
