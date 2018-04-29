{% extends "base.html" %}
{% load staticfiles %}

{% block title %} Crypto - market/pair details {% endblock %}
{% block pagename %} Crypto (app v.1) {% endblock %}

{% block content %}

<div class="container">
<div class="welcome-gridsinfo"></div>

<table class="table table-striped">
    <tr>
      <th>Pair</th>
      <th>Status</th>
      <th>Interval</th>
      <th>Period</th>
      <th>Notification</th>
      <th>Last update</th>
    </tr>
    <tr>
      <td>{{ pair.pair }}</td>
      <td>{{ pair.get_status }}</td>
      <td>{{ pair.get_interval }}</td>
      <td>{{ pair.get_period }}</td>
      <td>{{ pair.get_notification }}</td>
      <td>{{ pair.update_date }}</td>
    </tr>
</table>

<div class="contact-info-grids">

<table class="table table-striped">
    <tr>
      <th>From</th>
      <th>To</th>
      <th>Current status</th>
    </tr>
    <tr>
      <td>{{ rules.first.get_start_data }}</td>
      <td>{{ rules.first.get_end_data }}</td>
      <td>{{ rules.first.get_res_data }}</td>
    </tr>
</table>

<div class="contact-info-grids">

<p align="center"><b>RAW DATA</b></p>

<table class="table table-striped">
    <tr>
      <th>Pair information</th>
    </tr>
    <tr>
      <td>{{ pair.pair_info }}</td>
    </tr>
</table>

<table class="table table-striped">
    <tr>
      <th>24 hour price change statistics</th>
    </tr>
    <tr>
      <td>{{ pair.get_24h_ticker }}</td>
    </tr>
</table>

<table class="table table-striped">
    <tr>
      <th>Historical Klines (Kline/candlestick bars for a symbol. Klines are uniquely identified by their open time)</th>
    </tr>
    <tr>
      <td>{{ pair.historical_candlesticks }}</td>
    </tr>
</table>

<table class="table table-striped">
    <tr>
      <th>Market depth (Order Book for the market, rows: default 100; max 1000)</th>
    </tr>
    <tr>
      <td>{{ pair.market_depth }}</td>
    </tr>
</table>

<table class="table table-striped">
    <tr>
      <th>Recent trades (up to last 500)</th>
    </tr>
    <tr>
      <td>{{ pair.recent_trades }}</td>
    </tr>
</table>

<div class="contact-info-grids">

<a href="{% url 'crypto:stat_view' %}">Return to previous page</a>

</div>
</div>
</div>

{% endblock %}
