{% extends "base.html" %}
{% load staticfiles %}
{% load customtags %}

{% block title %} TC user media data {% endblock %}
{% block pagename %} Media data {% endblock %}

{% block content %}

<div class="container">
<div class="welcome-gridsinfo"></div>

<table class="table table-striped">
    <tr>
      <th>Username</th>
      <th>id</th>
      <th>tags</th>
      <th>media</th>
      <th>Updated</th>
  </tr>
{% for med in media %}
    <tr>
        <td>{{ med.username }}</a></td>
        <td>{{ med.media_id }}</td>
        <td>{{ med.media_tags }}</td>
        <td>{{ med.media }}</td>
        <td>{{ med.update_date }}</td>
    </tr>
{% endfor %}
</table>

</div>

{% endblock %}
