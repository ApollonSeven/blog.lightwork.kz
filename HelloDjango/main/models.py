from django.db import models

class Articles(models.Model):
    title = models.CharField(max_length = 100, verbose_name="Название статьи")
    description = models.CharField(max_length = 500, verbose_name="Краткое описание (500 символов)", null=True)
    meta_title = models.CharField(max_length = 300, verbose_name="Title", null=True)
    meta_descr = models.CharField(max_length = 300, verbose_name="Description для meta", null=True)
    content = models.TextField(verbose_name="Текст статьи (вводить сохраняя теги)")
    date = models.DateTimeField(verbose_name="Дата и время")
    img = models.ImageField(upload_to='images', null=True, verbose_name="Изображение статьи")
    alt_image = models.CharField(max_length = 30, verbose_name = "Alt для изображения статьи", null=True)
    slug = models.SlugField(primary_key=True, max_length=250, verbose_name="Красивая ссылка латиницей", null=False)
    author = models.CharField(max_length = 20, null=True, verbose_name="Автор статьи")
    pub_date = models.DateTimeField(null=True, auto_now=True)
    tag = models.ForeignKey('ArticleTags', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Статьи"

class ArticleTags(models.Model):
    title = models.CharField(max_length = 20, null=True, verbose_name="Тег")
    slug = models.CharField(max_length = 100, verbose_name="Slug", default="")
    color = models.CharField(max_length = 100, verbose_name="Цвет", default="")
    rgb = models.CharField(max_length = 100, verbose_name="RGB", default="")
    
    def __str__(self):
        return self.title

class Policy(models.Model):
    title = models.CharField(max_length = 200, null=True, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Текст статьи")
    
    def __str__(self):
        return self.title