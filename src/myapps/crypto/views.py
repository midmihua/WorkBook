from django.shortcuts import redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

from myapps.decorators import render_to

from .models import Stat, Pair
from myapps.crypto.markets.binan import Binance

import pandas as pd


# Instance of Binance market
cl = Binance()


@render_to('crypto/pages/stats.tpl')
def stat_view(request):

    # Retrieve all stats objects
    all_markets_coins = Stat.objects.all().order_by('market').order_by('pair')

    # Get Binance status
    market_status = cl.ping_server()

    # Get Pair information
    pair_info = dict()
    for market in all_markets_coins:
        pair_info[market.pair] = cl.get_pair_status(market.pair)

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
        'market_status': market_status,
        'pair_info': pair_info,
    }


# TBD
@render_to('crypto/pages/edit.tpl')
def edit(request, pair_id):
    return {
        'form': 'TBD: ' + pair_id
    }


@render_to('crypto/pages/details.tpl')
def details(request, pair_id):

    pair = get_object_or_404(Pair, pk=pair_id)

    # Get Pair info
    pair_info = cl.get_pair_info(str(pair))

    # Get Pair history
    # Debug
    history = cl.get_historical_klines(str(pair), '30m', '4 hour ago UTC')
    pair_hist = pd.DataFrame(history)
    print(pair_hist)

    return {
        'pair_info': pair_info,
        'pair_hist': history,
    }