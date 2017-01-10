from rest_framework.pagination import PageNumberPagination

from menu.config import PAGE_SIZE


class DefaultPagination(PageNumberPagination):
    page_size = PAGE_SIZE