BASE_URL = "https://www.kupi.cz"


def get_page_url(section, item_id: str = ""):
    return "{}/{}/{}".format(BASE_URL, section, item_id)


def in_range(value, min_value, max_value):
    return min_value <= value <= max_value
