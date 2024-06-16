from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Наименование категории",
        help_text="Введите наименование категории",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание категории",
        help_text="Введите описание категории",
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        max_length=50,
        verbose_name="Наименование продукта",
        help_text="Введите наименование продукта",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание продукта",
        help_text="Введите описание продукта",
    )
    preview = models.ImageField(
        upload_to="catalog/preview",
        blank=True,
        null=True,
        verbose_name="Изображение продукта",
        help_text="Загрузите изображение продукта",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория продукта",
        help_text="Введите категорию продукта",
        blank=True,
        null=True,
        related_name="products",
    )
    price_per_purchase = models.PositiveIntegerField(
        verbose_name="Цена за покупку", help_text="Введите цену",
    )
    created_at = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Дата создания продукта (записи в БД)",
        help_text="Введите дату создания продукта (записи в БД)",
    )
    updated_at = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Дата последнего изменения продукта (записи в БД)",
        help_text="Введите дату последнего изменения продукта (записи в БД)",
    )

    # manufactured_at = models.DateField(
    #     blank=True,
    #     null=True,
    #     verbose_name="Дата производства продукта",
    #     help_text="Введите дату производства продукта",
    # )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name"]

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name="Заголовок блога",
        help_text="Введите заголовок блога",
    )
    slug = models.CharField(
        max_length=50,
        verbose_name="Slug блога",
        help_text="Введите Slug блога",
        null=True, blank=True
    )
    content = models.TextField(
        blank=True,
        null=True,
        verbose_name="Содержание блога",
        help_text="Введите содержание блога",
    )
    preview = models.ImageField(
        upload_to="catalog/blog_preview",
        blank=True,
        null=True,
        verbose_name="Изображение",
        help_text="Загрузите изображение",
    )
    created_at = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name="Дата создания блога",
        help_text="Введите дату создания блога",
    )
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    is_published = models.BooleanField(default=True, verbose_name="Опубликован")
    views_count = models.IntegerField(default=0, verbose_name='просмотры')

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"

    def __str__(self):
        return self.title
