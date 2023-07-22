from unittest import TestCase

from utils.pagination import make_pagination_ranger


class PaginationTest(TestCase):
    def test_make_pagination_range_returns_a_pagination_range(self):
        pagination = make_pagination_ranger(
            page_range=list(range(1, 21)),
            qtd_pag=4,
            current_pag=1,
        )
        self.assertEqual([1, 2, 3, 4], pagination)
