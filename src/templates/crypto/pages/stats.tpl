{% extends "base.html" %}
{% load staticfiles %}

{% block title %} Crypto - all markets and coins {% endblock %}

{% block pagename %} Crypto (app v.1) {% endblock %}

{% block content %}

<div class="container">

<div class="welcome-gridsinfo"></div>

<table class="table table-striped">
    <tr>
      <th>ID (edit)</th>
      <th>Market</th>
      <th>Pair</th>
      <th>Interval</th>
      <th>Last update</th>
      <th>See details</th>
  </tr>
{% for stat in stats %}
    <tr>
        <td><a href="#" class="badge">{{ stat.id }}</a></td>
        <td>{{ stat.market }}</td>
        <td>{{ stat.pair }}</td>
        <td>{{ stat.interval }}</td>
        <td>{{ stat.update_date }}</td>
        <td><a href="#" class="badge">(?)</a></td>
    </tr>
{% endfor %}
</table>

{% if stats.has_other_pages %}
  <ul class="pagination">
    {% if stats.has_previous %}
      <li><a href="?page={{ stats.previous_page_number }}">&laquo;</a></li>
    {% else %}
      <li class="disabled"><span>&laquo;</span></li>
    {% endif %}
    {% for i in stats.paginator.page_range %}
      {% if stats.number == i %}
        <li class="active"><span>{{ i }} <span class="sr-only">(current)</span></span></li>
      {% else %}
        <li><a href="?page={{ i }}">{{ i }}</a></li>
      {% endif %}
    {% endfor %}
    {% if stats.has_next %}
      <li><a href="?page={{ stats.next_page_number }}">&raquo;</a></li>
    {% else %}
      <li class="disabled"><span>&raquo;</span></li>
    {% endif %}
  </ul>
{% endif %}

</div>

{% endblock %}
