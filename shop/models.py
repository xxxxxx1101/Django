from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=40, verbose_name='Фамилия')
    date_birthday = models.DateField(verbose_name='Дата рождения')
    date_of_death = models.DateField(null= True, blank= True , verbose_name='Дата смерти')
    description = models.TextField(verbose_name='Биография')

    def __str__(self) -> str:
        return self.first_name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = "Авторы"

    
class Book(models.Model):
    name = models.CharField(max_length=30, verbose_name='Название книги')
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='Автор')
    in_stock = models.BooleanField(default=True,verbose_name='В наличии')
    publication_date = models.DateField(verbose_name='Дата публикаци')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural="Книги"


class CategoryMovie(models.Model):
    name = models.CharField(max_length=30,unique=True, verbose_name='Название категории')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = 'Категория фильма'
        verbose_name_plural="Категория фильмов"


class Movie(models.Model):
    image = models.ImageField(upload_to='images/',verbose_name='фото')
    name = models.CharField(max_length=40, verbose_name='Название фильма')
    category = models.ForeignKey(CategoryMovie, on_delete=models.CASCADE, verbose_name='Категория')
    year_release = models.DateField(verbose_name='Дата релиза')
    company = models.CharField(max_length=30, verbose_name='Компания')
    time = models.IntegerField(verbose_name='Длительность')
    budget = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='Бюджет')
    description = models.TextField(verbose_name='Описание')

    def str(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural="Фильмы"


class User(models.Model):
    first_name = models.CharField(max_length=50,verbose_name='имя')
    login = models.CharField(max_length=50,verbose_name='Логин')
    email = models.EmailField(verbose_name='Почта')
    create = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.email}'
   
    class Meta:
        verbose_name = 'Пользыватель'
        verbose_name_plural = 'Пользыватели'


