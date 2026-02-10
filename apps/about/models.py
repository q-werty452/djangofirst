from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class About(models.Model):
    title = models.CharField(max_length=100, verbose_name="О нас")
    description = CKEditor5Field('Описание', config_name='extends')

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'О нас'


class Employee(models.Model):
    fullname = models.CharField(max_length=100, verbose_name="ФИО")
    image = models.ImageField(
        upload_to='staff/', verbose_name="фото/ава",
        null=True, blank=True
    )
    age = models.IntegerField(verbose_name="Возраст")
    position = models.CharField(max_length=50, verbose_name="Должность")
    exp = models.CharField(max_length=50, verbose_name="Опыт")
    slug = models.SlugField(unique=True, null=True)

    def __str__(self):
        return self.fullname
    
    class Meta:
        verbose_name_plural = 'Сотрудники'


class SocialLink(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Название соцсети", max_length=100)
    link = models.CharField(max_length=255, verbose_name="Ссылка на аккаунт")

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Соцсети сотрудников'