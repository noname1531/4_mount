# Generated by Django 5.0.4 on 2024-04-20 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0003_about'),
    ]

    operations = [
        migrations.DeleteModel(
            name='About',
        ),
        migrations.AlterModelOptions(
            name='settings',
            options={'verbose_name': 'Места где нужно заменрть фото  ', 'verbose_name_plural': 'Места где нужно заменрть фото '},
        ),
        migrations.AddField(
            model_name='settings',
            name='photo2',
            field=models.ImageField(default=1, upload_to='logo/image', verbose_name='Фотография'),
            preserve_default=False,
        ),
    ]
