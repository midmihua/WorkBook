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

<p>List of words</p>

<p><a href="{% url 'english:add_words' %}">New word</a></p>

<table style="width:100%">
    <tr>
      <th>word_id</th>
      <th>word</th>
      <th>translation</th>
      <th>comment</th>
      <th>create_date</th>
      <th>update_date</th>
      <th></th>
  </tr>
{% for word in list_of_words %}
    <tr>
        <td><a href="{% url 'english:edit_words' word.id %}">{{ word.id }}</a></td>
        <td>{{ word.word }}</td>
        <td>{{ word.translation }}</td>
        <td>{{ word.comment }}</td>
        <td>{{ word.create_date }}</td>
        <td>{{ word.update_date }}</td>
        <td><a href="{% url 'english:delete_words' word.id %}">[x]</a></td>
    </tr>
{% endfor %}
</table>

<p><a href="{% url 'english:add_words' %}">New word</a></p>

</body>
</html>
