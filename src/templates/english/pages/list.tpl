{% extends "base.html" %}
{% load staticfiles %}

{% block title %} English notebook {% endblock %}


{% block content %}


<div class="welcome-gridsinfo">
    <a href="{% url 'english:add_words' %}"><b>[ Add new word ]</b></a>
</div>

<div class="col-lg-6 in-gp-tb">
    <div class="input-group">
      <input type="text" class="form-control" placeholder="Search for...">
      <span class="input-group-btn">
        <button class="btn btn-default" type="button">Go!</button>
      </span>
    </div>
</div>

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

<br/>

{% endblock %}
