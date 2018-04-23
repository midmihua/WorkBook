from django.shortcuts import redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

from myapps.decorators import render_to

from .models import Stat


@render_to('crypto/pages/stats.tpl')
def stat_view(request):

    # Retrieve all stats objects
    all_markets_coins = Stat.objects.all().order_by('market').order_by('pair')

    # Pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(all_markets_coins, 10)

    try:
        one_page_stats = paginator.page(page)
    except PageNotAnInteger:
        one_page_stats = paginator.page(1)
    except EmptyPage:
        one_page_stats = paginator.page(paginator.num_pages)

    return {
        'stats': one_page_stats
    }
