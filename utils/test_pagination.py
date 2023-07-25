from unittest import TestCase

from utils.pagination import make_pagination_ranger


class PaginationTest(TestCase):
    def test_make_pagination_range_returns_a_pagination_range(self):
        pagination = make_pagination_ranger(
            page_range=list(range(1, 21)),
            qtd_pag=4,
            current_pag=1,
        )['pagination']
        self.assertEqual([1, 2, 3, 4], pagination)

    def test_first_range_is_static_if_current_page_is_less_than_middle_page(self):  # noqa: E501

        pagination = make_pagination_ranger(
            page_range=list(range(1, 21)),
            qtd_pag=4,
            current_pag=1,
        )['pagination']
        self.assertEqual([1, 2, 3, 4], pagination)

        pagination = make_pagination_ranger(
            page_range=list(range(1, 21)),
            qtd_pag=4,
            current_pag=2,
        )['pagination']
        self.assertEqual([1, 2, 3, 4], pagination)

        pagination = make_pagination_ranger(
            page_range=list(range(1, 21)),
            qtd_pag=4,
            current_pag=3,
        )['pagination']
        self.assertEqual([2, 3, 4, 5], pagination)

        pagination = make_pagination_ranger(
            page_range=list(range(1, 21)),
            qtd_pag=4,
            current_pag=4,
        )['pagination']
        self.assertEqual([3, 4, 5, 6], pagination)

    def test_make_sure_middle_ranges_are_correct(self):  # noqa: E501

        pagination = make_pagination_ranger(
            page_range=list(range(1, 21)),
            qtd_pag=4,
            current_pag=10,
        )['pagination']
        self.assertEqual([9, 10, 11, 12], pagination)

        pagination = make_pagination_ranger(
            page_range=list(range(1, 21)),
            qtd_pag=4,
            current_pag=12,
        )['pagination']
        self.assertEqual([11, 12, 13, 14], pagination)

    def test_make_pagination_range_is_static_when_last_page_is_netx(self):  # noqa: E501

        pagination = make_pagination_ranger(
            page_range=list(range(1, 21)),
            qtd_pag=4,
            current_pag=18,
        )['pagination']
        self.assertEqual([17, 18, 19, 20], pagination)

        pagination = make_pagination_ranger(
            page_range=list(range(1, 21)),
            qtd_pag=4,
            current_pag=19,
        )['pagination']
        self.assertEqual([17, 18, 19, 20], pagination)

        pagination = make_pagination_ranger(
            page_range=list(range(1, 21)),
            qtd_pag=4,
            current_pag=20,
        )['pagination']
        self.assertEqual([17, 18, 19, 20], pagination)

        pagination = make_pagination_ranger(
            page_range=list(range(1, 21)),
            qtd_pag=4,
            current_pag=21,
        )['pagination']
        self.assertEqual([17, 18, 19, 20], pagination)
