from django.contrib.auth.models import User
from django.test import TestCase

from testimonials.models import Category, Testimony


class TestimonialsTestBase(TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def make_Category(self, name='Category') -> Category:
        return Category.objects.create(name=name)

    def make_autor(self, first_name='user',
                   last_name='name', username='username',
                   password='123456', email='user@email.com'
                   ) -> User:
        return User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            password=password,
            email=email
        )

    def make_Testimony(self,
                       Category_data=None,
                       author_data=None,
                       title='Testimony titulo',
                       description='Descrição Testimony',
                       slug='Testimony-slug',
                       testimony='testimony',
                       published=True,
                       ) -> Testimony:
        if Category_data is None:
            Category_data = {}

        if author_data is None:
            author_data = {}

        return Testimony.objects.create(
            Category=self.make_Category(**Category_data),
            author=self.make_autor(**author_data),
            title=title,
            description=description,
            slug=slug,
            testimony=testimony,
            published=published,
        )
