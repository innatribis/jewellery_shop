from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Название категории')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name='Код категории (создаётся автоматически)')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('jewellery_shop:product_list_by_category',
                        args=[self.slug])

class Finishing(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Название отделки')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name='Код отделки (создаётся автоматически)')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Отделка'
        verbose_name_plural = 'Отделки'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('jewellery_shop:product_list_by_finishing',
                        args=[self.slug])


class Collection(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Название коллекции')
    slug = models.SlugField(max_length=200, db_index=True, unique=True, verbose_name='Код коллекции (создаётся автоматически)')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('jewellery_shop:product_list_by_collection',
                        args=[self.slug])

class Gem(models.Model):
    COLORS = [
        ('red', 'красный'),
        ('orange', 'оранжевый'),
        ('yellow', 'жёлтый'),
        ('green', 'зелёный'),
        ('sky blue', 'голубой'),
        ('blue', 'синий'),
        ('purple', 'фиолетовый'),
        ('white', 'белый'),
        ('black', 'чёрный'),
        ('brown', 'коричневый'),
        ('pink', 'розовый')
    ]
    name = models.CharField(max_length=200, db_index=True, verbose_name='Название драгоценного камня')
    slug = models.SlugField(max_length=200, db_index=True, verbose_name='Код драгоценного камня (создаётся автоматически)')
    clarity = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(12)], verbose_name='Чистота')
    color = models.CharField(max_length=8, choices=COLORS, verbose_name='Цвет')

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Драгоценный камень'
        verbose_name_plural = 'Драгоценные камни'

    def __str__(self):
        return self.name + '. Чистота ' + str(self.clarity) + '. Цвет: ' + self.get_color_display()

class Metal(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='Название металла')
    slug = models.SlugField(max_length=200, db_index=True, verbose_name='Код металла (создаётся автоматически)')
    alloy = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(1000)], verbose_name='Проба')

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Металл'
        verbose_name_plural = 'Металлы'

    def __str__(self):
        return self.name + '. Проба: ' + str(self.alloy)


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.PROTECT, verbose_name='Категория ювелирного изделия')
    collection = models.ForeignKey(Collection, related_name='products', on_delete=models.SET_NULL, verbose_name='Коллекция ювелирных изделий', blank=True, null=True)
    name = models.CharField(max_length=200, db_index=True, verbose_name='Название ювелирного изделия')
    slug = models.SlugField(max_length=200, db_index=True, verbose_name='Код ювелирного изделия (создаётся автоматически)')
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True, verbose_name='Фото')
    description = models.TextField(blank=True, verbose_name='Описание')
    weight = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Вес одного ювелирного изделия')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    available = models.BooleanField(default=True, verbose_name='Доступность')
    finishings = models.ManyToManyField(Finishing, blank=True)
    

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name = 'Ювелирное изделие'
        verbose_name_plural = 'Ювелирные изделия'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('jewellery_shop:product_detail',
                        args=[self.id, self.slug])

class Gems_for_Products(models.Model):
    CUTS = [
        ('c1', 'круг'),
        ('c2', 'груша'),
        ('c3', 'овал'),
        ('c4', 'маркиз'),
        ('c5', 'сердце'),
        ('c6', 'принцесса'),
        ('c7', 'изумруд'),
        ('c8', 'багет'),
        ('c9', 'квадрат'),
        ('c10', 'восьмиугольник'),
        ('c11', 'французская'),
        ('c12', 'античная')
        ]
    product = models.ForeignKey(Product, related_name='gems_for_Products', on_delete=models.CASCADE, verbose_name='Ювелирное изделие')
    gem = models.ForeignKey(Gem, on_delete=models.CASCADE, verbose_name='Драгоценный камень')
    weight = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Вес одного камня')
    cut = models.CharField(max_length=3, choices=CUTS, verbose_name='Огранка камня')
    count = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(100)], verbose_name='Количество камней в одном изделии')

    class Meta:
        verbose_name = 'Драгоценные камни в ювелирном изделии'
        verbose_name_plural = 'Драгоценные камни в ювелирных изделиях'

class Metals_for_Products(models.Model):
    product = models.ForeignKey(Product, related_name='metals_for_Products', on_delete=models.CASCADE, verbose_name='Ювелирное изделие')
    metal = models.ForeignKey(Metal, on_delete=models.CASCADE, verbose_name='Металл')
    weight = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Вес металла в одном изделии')

    class Meta:
        verbose_name = 'Металлы в ювелирном изделии'
        verbose_name_plural = 'Металлы в ювелирных изделиях'

