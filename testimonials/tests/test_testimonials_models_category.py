from django.core.exceptions import ValidationError
from django.http.request import T
from tests.test_testimonials_base import TestimonialsTestBase


class TestimonyModelCatergoryTest(TestimonialsTestBase):
    def setUp(self) -> None:
        self.category = self.make_category(
            nome='Testing Category'
        )
        return super().setUp()

    def test_test_category_representation_string(self):
        self.assertEqual(
            str(self.category),
            self.category.name
        )

    def test_test_category_model_max_length(self):
        self.category.name = 'A' * 51
        with self.assertRaises(ValidationError):
            self.category.full_clean()
