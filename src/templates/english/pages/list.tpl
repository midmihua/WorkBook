{% extends "base.html" %}
{% load staticfiles %}

{% block title %} English notebook - list of words {% endblock %}

{% block pagename %} English {% endblock %}

{% block content %}

<div class="container">

<div class="welcome-gridsinfo">
    <a href="{% url 'english:add_words' %}"><b>[ Add new word ]</b></a>
</div>

<form action="" method="post">
{% csrf_token %}
<div class="col-lg-6 in-gp-tb">
    <div class="input-group">
      <input name="search_word" type="text" class="form-control" placeholder="Search for...">
      <span class="input-group-btn">
        <button class="btn btn-default" type="submit">Go!</button>
      </span>
    </div>
</div>

</form>

<table class="table table-striped">
    <tr>
      <th>ID (edit)</th>
      <th>Word</th>
      <th>Translation</th>
      <th>Comment</th>
      <th>Update date</th>
      <th>(delete)</th>
  </tr>
{% for word in list_of_words %}
    <tr>
        <td><a href="{% url 'english:edit_words' word.id %}" class="badge">{{ word.id }}</a></td>
        <td>{{ word.word }}</td>
        <td>{{ word.translation }}</td>
        <td>{{ word.comment }}</td>
        <td>{{ word.update_date }}</td>
        <td><a href="{% url 'english:delete_words' word.id %}" class="badge">[x]</a></td>
    </tr>
{% endfor %}
</table>

{% if list_of_words.has_other_pages %}
  <ul class="pagination">
    {% if list_of_words.has_previous %}
      <li><a href="?page={{ list_of_words.previous_page_number }}">&laquo;</a></li>
    {% else %}
      <li class="disabled"><span>&laquo;</span></li>
    {% endif %}
    {% for i in list_of_words.paginator.page_range %}
      {% if list_of_words.number == i %}
        <li class="active"><span>{{ i }} <span class="sr-only">(current)</span></span></li>
      {% else %}
        <li><a href="?page={{ i }}">{{ i }}</a></li>
      {% endif %}
    {% endfor %}
    {% if list_of_words.has_next %}
      <li><a href="?page={{ list_of_words.next_page_number }}">&raquo;</a></li>
    {% else %}
      <li class="disabled"><span>&raquo;</span></li>
    {% endif %}
  </ul>
{% endif %}

</div>

{% endblock %}
