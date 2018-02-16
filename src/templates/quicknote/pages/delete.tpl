{% extends "base.html" %}
{% load staticfiles %}

{% block title %} Quick Note - delete note {% endblock %}

{% block content %}

<div class="container">
<div class="contact-info cf-1">
<div class="contact-info-grids">

<form action="#" method="post">
    {% csrf_token %}
    {{ form.management_form }}
    {{ form.note }}
    <input type="submit" value="DELETE THE WORD?"> / <a href="{% url 'quicknote:list_notes' %}">Return to the list</a>
</form>

</div>
</div>
</div>

{% endblock %}
