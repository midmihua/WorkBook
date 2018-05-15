from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from myapps.decorators import render_to
from .models import TCUser, TCUserMedia


@render_to('tryinsta/pages/users.tpl')
def users(request):

    # Retrieve all tc_user objects
    tc_users = TCUser.objects.all()

    # Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(tc_users, 10)

    try:
        one_page_users = paginator.page(page)
    except PageNotAnInteger:
        one_page_users = paginator.page(1)
    except EmptyPage:
        one_page_users = paginator.page(paginator.num_pages)

    return {
        'tc_users': one_page_users,
    }


@render_to('tryinsta/pages/media.tpl')
def user_media(request, tc_user_id):

    media = get_object_or_404(TCUserMedia, username_id=tc_user_id)

    return {
        'media': media,
    }


