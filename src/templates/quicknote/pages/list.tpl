{% extends "base.html" %}
{% load staticfiles %}

{% block title %} Quick Note - list of notes {% endblock %}

{% block pagename %} Quick note {% endblock %}

{% block content %}

<div class="container">

<div class="welcome-gridsinfo">
    <a href="{% url 'quicknote:add_note' %}"><b>[ Quick note ]</b></a>
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
      <th>Note</th>
      <th>File</th>
      <th>Update date</th>
      <th>(delete)</th>
  </tr>
{% for note in notes %}
    <tr>
        <td><a href="{% url 'quicknote:edit_note' note.id %}" class="badge">{{ note.id }}</a></td>
        <td>{% autoescape off %} {{ note.note }} {% endautoescape %}</td>
        <td>{{ note.file }}</td>
        <td>{{ note.update_date }}</td>
        <td><a href="{% url 'quicknote:delete_note' note.id %}" class="badge">[x]</a></td>
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
