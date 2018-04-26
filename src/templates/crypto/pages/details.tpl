{% extends "base.html" %}
{% load staticfiles %}

{% block title %} Crypto - market/pair details {% endblock %}
{% block pagename %} Crypto (app v.1) {% endblock %}

{% block content %}

<div class="container">
<div class="welcome-gridsinfo"></div>

<table class="table table-striped">
    <tr>
      <th><font color="blue">symbol</font></th>
      <th>{{ pair_info.symbol }}</th>
    </tr>
    <tr>
      <th><font color="blue">baseAsset</font></th>
      <th>{{ pair_info.baseAsset }}</th>
    </tr>
    <tr>
      <th><font color="blue">quoteAsset</font></th>
      <th>{{ pair_info.quoteAsset }}</th>
    </tr>
    <tr>
      <th><font color="blue">orderTypes</font></th>
      <th>{{ pair_info.orderTypes }}</th>
    </tr>
    <tr>
      <th><font color="blue">filters</font></th>
      <th>{{ pair_info.filters }}</th>
    </tr>
    <tr>
      <th><font color="blue">status</font></th>
      <th>{{ pair_info.status }}</th>
    </tr>
</table>

<div class="contact-info-grids">

<table>
{%for line in pair_hist %}
<tr>
    <th>{{ line }}</th>
</tr>
{% endfor %}
</table>

<div class="contact-info-grids">

<a href="{% url 'crypto:stat_view' %}">Return to the list</a>

</div>
</div>
</div>

{% endblock %}
