from re import T

from django.core.exceptions import ValidationError
from parameterized import parameterized

from .test_testimonials_base import TestimonialsTestBase, Testimony


class TestimonialsModelTest(TestimonialsTestBase):
    def setUp(self) -> None:
        self.testimony = self.make_testimony()
        return super().setUp()

    def make_testimony_no_defaults(self):
        testimony = Testimony(
            category=self.make_categoria(name='Test category pattern'),
            autor=self.make_autor(username='newuser'),
            title='Testimonial title',
            description='Testimonial Description',
            slug='Testimonio-slug',
            testimony='Testimony',
            published=True,
            photo=None
        )
        testimony.full_clean()
        testimony.save()
        return testimony

    @parameterized.expand([
        ('title', 77),
        ('description', 165)
    ])
    def test_testimony_todos_campos_max_length(self, field, max_length):
        setattr(self.testimony, field, 'A' * (max_length + 10))
        with self.assertRaises(ValidationError):
            self.testimony.full_clean()

    def test_test_representation_string(self):
        phrase = 'Test representation'
        self.testimony.title = 'Test representation'
        # self.testimony.full_clean()
        self.testimony.save()
        self.assertEqual(
            str(self.testimony), phrase,
            msg=f'the recipe string representation must be '
            f'"{phrase}" but this arrived "{str(self.testimony)}" '
        )
