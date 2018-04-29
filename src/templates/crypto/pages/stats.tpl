{% extends "base.html" %}
{% load staticfiles %}
{% load customtags %}

{% block title %} Crypto - all markets and coins {% endblock %}
{% block pagename %} Crypto (app v.1) {% endblock %}

{% block content %}

<div class="container">
<div class="welcome-gridsinfo"></div>

<table class="table table-striped">
    <tr>
      <th>Edit</th>
      <th>Pair</th>
      <th>Status</th>
      <th>Interval</th>
      <th>Period</th>
      <th>Send notification</th>
      <th>Last update</th>
      <th>Details</th>
  </tr>
{% for stat in stats %}
    <tr>
        <td><a href="{% url 'crypto:edit' stat.id %}" class="badge">{{ stat.id }}</a></td>
        <td>{{ stat.pair }}</td>
        <td>{{ stat.get_status }}</td>
        <td>{{ stat.get_interval }}</td>
        <td>{{ stat.get_period }}</td>
        <td>{{ stat.get_notification }}</td>
        <td>{{ stat.update_date }}</td>
        <td><a href="{% url 'crypto:details' stat.id %}" class="badge">(?)</a></td>
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
