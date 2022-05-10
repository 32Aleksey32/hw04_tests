from django.core.paginator import Paginator


def paginate_page(queryset, request):
    count_posts = 10
    paginator = Paginator(queryset, count_posts)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj
