{% extends "base.html" %}
{% load staticfiles %}

{% block title %} English notebook - add new {% endblock %}

{% block content %}

<div class="container">
<div class="contact-info cf-1">
<div class="contact-info-grids">

<form action="{% url 'english:add_words' %}" method="post">
{% csrf_token %}
	<input type="text" placeholder="New word" name="word" required maxlength="1000" id="id_word" >
	<input type="text" placeholder="Translation" name="translation" required id="id_translation">
	<textarea placeholder="Comment" name="comment" id="id_comment"></textarea>
	<input type="submit" value="SAVE NEW WORD"> / <a href="{% url 'english:list_words' %}">Return to the list</a>
</form>

</div>
</div>
</div>

{% endblock %}
