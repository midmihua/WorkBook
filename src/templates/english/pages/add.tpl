<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>List of English words</title>
    <style>
        table, th, td {
        border: 1px solid black;
        border-collapse: collapse;
        }
        th, td {
        padding: 10px;
        }
    </style>
</head>
<body>

<p>New word</p>

{% block content %}

<form action="{% url 'english:add_words' %}" method="post">
    {% csrf_token %}
    <table>
        <tr>
            <th>Word</th>
            <th>Translation</th>
            <th>Comment</th>
        </tr>
        {{ form.management_form }}
        <tr>
            <td> {{ form.word }} </td>
            <td> {{ form.translation }} </td>
            <td> {{ form.comment }} </td>
        </tr>
    </table>

    <br>
    <input type="submit" value="Add">

    <br>
    <p><a href="{% url 'english:list_words' %}">Return to the list</a></p>

</form>

{% endblock %}
