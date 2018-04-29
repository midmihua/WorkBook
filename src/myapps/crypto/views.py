from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from myapps.decorators import render_to

from .models import Stat, RuleMap


# Constants
STATUS_ACTIVE = 'AC'


@render_to('crypto/pages/stats.tpl')
def stat_view(request):

    # Retrieve all stats objects
    all_markets_coins = Stat.objects.filter(status=STATUS_ACTIVE).order_by('pair')

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
        'stats': one_page_stats,
    }


@render_to('crypto/pages/details.tpl')
def details(request, pair_id):

    pair = get_object_or_404(Stat, pk=pair_id)
    # temporary
    rules = RuleMap.objects.filter(stat=pair_id)

    return {
        'pair': pair,
        'rules': rules
    }


# TBD
@render_to('crypto/pages/edit.tpl')
def edit(request, pair_id):

    return {
        'form': 'not implemented yet: ' + pair_id
    }
