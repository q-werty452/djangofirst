from django.db import models
from django_ckeditor_5.fields import CKEditor5Field
from django.contrib.auth.models import User
from django.utils.text import slugify


class Category(models.Model):
    title = models.CharField(
        max_length=100, verbose_name="Название категории"
    )
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Категории' 


class News(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)   

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, 
        verbose_name="Категория", null=True
    )
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    image = models.ImageField(
        upload_to='newsmedia/', null=True, verbose_name="Фото"
    )
    description = CKEditor5Field('Описание', config_name='extends')
    slug = models.SlugField(unique=True, null=True)



def save(self, *args, **kwargs):
    if not self.slug:
        base_slug = slugify(self.title)
        slug = base_slug
        counter = 1
        while News.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        self.slug = slug
    super().save(*args, **kwargs)



    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Новости'
        ordering=['-id']


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(verbose_name="ФИО", max_length=100)
    text = models.TextField(verbose_name='Комментарии')
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Комментарии'
        verbose_name = 'коммент'