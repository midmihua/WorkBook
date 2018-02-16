{% extends "base.html" %}
{% load staticfiles %}

{% block title %} Quick Note - edit note {% endblock %}

{% block content %}

<div class="container">
<div class="contact-info cf-1">
<div class="contact-info-grids">

<form action="#" method="post" enctype="multipart/form-data">
    {% csrf_token %}
    {{ form.management_form }}
    {{ form.note }}
    {{ form.file }}
    <input type="submit" value="SAVE CHANGES"> / <a href="{% url 'quicknote:list_notes' %}">Return to the list</a>
</form>

</div>
</div>
</div>

{% endblock %}
