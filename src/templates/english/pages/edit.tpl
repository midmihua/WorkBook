{% extends "base.html" %}
{% load staticfiles %}

{% block title %} English notebook - edit page {% endblock %}

{% block content %}

<div class="container">
<div class="contact-info cf-1">
<div class="contact-info-grids">

<form action="#" method="post">
    {% csrf_token %}
    {{ form.management_form }}
    {{ form.word }}
    {{ form.translation }}
    {{ form.comment }}
    <input type="submit" value="SAVE CHANGES"> / <a href="{% url 'english:list_words' %}">Return to the list</a>
</form>

</div>
</div>
</div>

{% endblock %}
