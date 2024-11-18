from django.db import models
from django.urls import reverse


def main_photo_upload_path(instance, filename):
    return f'main_photo/{filename}'

def certificate_upload_path(instance, filename):
    return f'certificates/{filename}'

class MainPhoto(models.Model):
    image = models.ImageField(upload_to=main_photo_upload_path)

    def __str__(self):
        # Показать только имя файла
        return self.image.name.split('/')[-1]

    class Meta:
        verbose_name = "Основное фото"
        verbose_name_plural = "Основные фото"

class MainText(models.Model):
    text = models.TextField(max_length=10000)

    def __str__(self):
        return self.text[:50] + ('...' if len(self.text) > 50 else '')

    class Meta:
        verbose_name = "Основной текст"
        verbose_name_plural = "Основные тексты"

class Links(models.Model):
    link = models.CharField(max_length=200, unique=True, verbose_name='Ссылка')

    def __str__(self):
        return self.link



    class Meta:
        verbose_name = "Полезная ссылка"
        verbose_name_plural = "Полезные ссылки"


class Certificates(models.Model):
    certificate = models.ImageField(upload_to=certificate_upload_path)

    def __str__(self):
        return self.certificate.name.split('/')[-1]

    class Meta:
        verbose_name = "Грамота"
        verbose_name_plural = "Грамоты"


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    cover_photo = models.ImageField(upload_to='articles_files/cover_photos', blank=False)
    datetime = models.DateField(auto_now=True)
    slug = models.SlugField(max_length=150)

    def get_absolute_url(self):
        return reverse("articles:show_article", kwargs={"article_slug": self.slug})
    
    def __str__(self):
        return self.title

class ArticleFiles(models.Model):
    image = models.ImageField(upload_to='articles_files/photos')
    article = models.ForeignKey('Article', on_delete=models.CASCADE, related_name='photos')

    def __str__(self):
        return self.image.name