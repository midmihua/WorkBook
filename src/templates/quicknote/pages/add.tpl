{% extends "base.html" %}
{% load staticfiles %}

{% block title %} Quick Note - add new {% endblock %}

{% block content %}

<div class="container">
<div class="contact-info cf-1">
<div class="contact-info-grids">

<form method="post" enctype="multipart/form-data" action="{% url 'quicknote:add_note' %}">
{% csrf_token %}
{{ form.as_p }}
<input type="submit" value="SAVE NOTE"> / <a href="{% url 'quicknote:list_notes' %}">Return to the list</a>
</form>

</div>
</div>
</div>

{% endblock %}
