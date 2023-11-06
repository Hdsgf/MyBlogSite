from django.db import models

# Create your models here.
class Post(models.Model):
    '''данные о посте'''
    title = models.CharField('Заголовок записи', max_length=100)
    description = models.TextField("Текст записи")
    author = models.CharField("Автор", max_length=15)
    date = models.DateField("Дата публикации")
    img = models.ImageField("Изображение", upload_to='image/%Y')

    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = "Запись"
        verbose_name_plural = "Записи"


class Comments(models.Model):
    '''коментарии'''
    email = models.EmailField()
    name= models.CharField('Имя', max_length=20)
    text_comments = models.TextField('Текст коментария', max_length=1000)
    post = models.ForeignKey(Post, verbose_name="Публикация", on_delete=models.CASCADE) #on_delete = все объекты которые ссылаются на удаленный объект тоже будут удалены

    def __str__(self):
        return f'{self.name}, {self.post}'

    class Meta:
        verbose_name = "Коментарий"
        verbose_name_plural = "Коментарии"
