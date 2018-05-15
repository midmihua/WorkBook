{% extends "base.html" %}
{% load staticfiles %}
{% load customtags %}

{% block title %} TC users {% endblock %}
{% block pagename %} List of TC users {% endblock %}

{% block content %}

<div class="container">
<div class="welcome-gridsinfo"></div>

<table class="table table-striped">
    <tr>
      <th>Username</th>
      <th>Token</th>
      <th>Updated</th>
  </tr>
{% for tc_user in tc_users %}
    <tr>
        <td><a href="{% url 'tryinsta:user_media' tc_user.id %}" class="badge">{{ tc_user.username }}</a></td>
        <td>{{ tc_user.token }}</td>
        <td>{{ tc_user.update_date }}</td>
    </tr>
{% endfor %}
</table>

{% if tc_users.has_other_pages %}
  <ul class="pagination">
    {% if tc_users.has_previous %}
      <li><a href="?page={{ tc_users.previous_page_number }}">&laquo;</a></li>
    {% else %}
      <li class="disabled"><span>&laquo;</span></li>
    {% endif %}
    {% for i in tc_users.paginator.page_range %}
      {% if tc_users.number == i %}
        <li class="active"><span>{{ i }} <span class="sr-only">(current)</span></span></li>
      {% else %}
        <li><a href="?page={{ i }}">{{ i }}</a></li>
      {% endif %}
    {% endfor %}
    {% if tc_users.has_next %}
      <li><a href="?page={{ tc_users.next_page_number }}">&raquo;</a></li>
    {% else %}
      <li class="disabled"><span>&raquo;</span></li>
    {% endif %}
  </ul>
{% endif %}

</div>

{% endblock %}
