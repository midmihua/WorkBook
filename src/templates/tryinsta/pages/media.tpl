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
      <th>Media</th>
      <th>Updated</th>
  </tr>
    <tr>
        <td>{{ media.username }}</a></td>
        <td>{{ media.media }}</td>
        <td>{{ media.update_date }}</td>
    </tr>
</table>

</div>

{% endblock %}
