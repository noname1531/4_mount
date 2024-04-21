# Generated by Django 5.0.4 on 2024-04-20 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0004_delete_about_alter_settings_options_settings_photo2'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='descriptions2',
            field=models.TextField(default=1, verbose_name='Описание сайта2'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settings',
            name='name2',
            field=models.CharField(default=1, max_length=255, verbose_name='Загаловок2'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='settings',
            name='photo3',
            field=models.ImageField(default=1, upload_to='logo/image', verbose_name='Фотография3'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='settings',
            name='photo2',
            field=models.ImageField(upload_to='logo/image', verbose_name='Фотография2'),
        ),
    ]