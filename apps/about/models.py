from django.db import models

# Create your models here.
class Settings(models.Model):
    name = models.CharField(
        max_length=255,
        verbose_name="Загаловок"
    )
    photo = models.ImageField(
        upload_to='logo/image',
        verbose_name="Фото"
    )
    descriptions = models.TextField(
        verbose_name="Описание сайта"
    )
    photo2 = models.ImageField(
        upload_to='logo/image',
        verbose_name="Фотография2"
    )
    name2 = models.CharField(
        max_length=255,
        verbose_name="Загаловок2"
    )
    descriptions2 = models.TextField(
        verbose_name="Описание сайта2"
    )
    photo3 = models.ImageField(
        upload_to='logo/image',
        verbose_name="Фотография3"
    )
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = "Места где нужно заменрть фото  "
        verbose_name_plural = "Места где нужно заменрть фото "

