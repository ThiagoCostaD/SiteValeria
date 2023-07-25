import math


def make_pagination_ranger(
    page_range,
    qtd_pag,
    current_pag,
):
    middle_range = math.ceil(qtd_pag/2)
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
