from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(
        max_length=50, help_text='Category name')

    def __str__(self):
        return self.nome


class Testimony(models.Model):

    title = models.CharField(
        max_length=77, help_text='Testimonial title', blank=False)

    description = models.CharField(
        max_length=165, help_text='Description of the testimony', blank=False)

    slug = models.SlugField(
        help_text='Slug do Testimonial', blank=False, unique=True)

    testimony = models.TextField(help_text='Text do testimony', blank=False)

    date_creation = models.DateTimeField(
        auto_now_add=True, help_text='Testimony creation date')

    modification_date = models.DateTimeField(
        auto_now=True, help_text='Testimony modification date')

    published = models.BooleanField(
        default=False,
        help_text='Indicates whether the testimony is published or not')

    photos = models.ImageField(
        upload_to='testimonys/img/%Y/%m/%d/', help_text='Testimonial photo')

    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True,
        blank=True, default=None, help_text='Testimony category',
        related_name='testimonys', related_query_name='testimony_category'
    )

    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True,
        blank=True, default=None, help_text='Author of the testimony',
        related_name='testimonys', related_query_name='testimony_author'
    )

    class Meta:
        verbose_name: str = 'testimony'
        verbose_name_plural: str = 'testimonys'
        ordering: list[str] = ['-date_creation']

    def __str__(self) -> str:
        return self.title
