import math

from django.core.paginator import Paginator


def make_pagination_range(
    page_range,
    qtd_pag,
    current_pag,
):
    middle_range = math.ceil(qtd_pag / 2)
    star_range = current_pag - middle_range
    stop_range = current_pag + middle_range
    total_pages = len(page_range)

    star_range_offset = abs(star_range) if star_range < 0 else 0

    if star_range < 0:
        star_range = 0
        stop_range += star_range_offset

    if stop_range >= total_pages:
        star_range = star_range - abs(total_pages - stop_range)

    pagination = page_range[star_range:stop_range]

    return {
        'pagination': pagination,
        'page_range': page_range,
        'qtd_pag': qtd_pag,
        'current_pag': current_pag,
        'total_pages': total_pages,
        'star_range': star_range,
        'stop_range': stop_range,
        'first_page_out_of_range': current_pag > middle_range,
        'last_page_out_of_range': stop_range > stop_range,
    }


def make_pagination(request, queryset, per_page, qty_page=4):

    try:
        current_page = int(request.GET.get('page', 1))
    except ValueError:
        current_page = 1

    paginator = Paginator(queryset, per_page)
    page_obj = paginator.get_page(current_page)

    pagination_range = make_pagination_range(
        paginator.page_range,
        qty_page,
        current_page
    )

    return page_obj, pagination_range
