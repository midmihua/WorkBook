from myapps.decorators import render_to
from .models import Words


@render_to('english/pages/list.tpl')
def list_words(request):
    list_of_words = Words.objects.all()
    return {
        'list_of_words': list_of_words
    }


@render_to('english/pages/add.tpl')
def add_words(request):
    return {
        'f_name': 'add_words'
    }


@render_to('english/pages/edit.tpl')
def edit_words(request, word_id):
    return {
        'f_name': 'edit_words'
    }


@render_to('english/pages/delete.tpl')
def delete_words(request, word_id):
    return {
        'f_name': 'delete_words'
    }
