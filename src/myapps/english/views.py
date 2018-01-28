from django.shortcuts import redirect, get_object_or_404

from myapps.decorators import render_to

from .models import Words
from .forms import AddNewWord, EditWord, DeleteWord


@render_to('english/pages/list.tpl')
def list_words(request):
    list_of_words = Words.objects.all().order_by('word')
    return {
        'list_of_words': list_of_words
    }


@render_to('english/pages/add.tpl')
def add_words(request):
    form = AddNewWord(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('english:list_words')
        else:
            form = AddNewWord()
    return {
        'form': form
    }


@render_to('english/pages/edit.tpl')
def edit_words(request, word_id):
    word = get_object_or_404(Words, pk=word_id)
    form = EditWord(request.POST or None, instance=word)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('english:list_words')
        else:
            form = EditWord(instance=word)
    return {
        'form': form
    }


@render_to('english/pages/delete.tpl')
def delete_words(request, word_id):
    word = get_object_or_404(Words, pk=word_id)
    form = DeleteWord(request.POST or None, instance=word)
    if request.method == 'POST':
        if form.is_valid():
            word.delete()
            return redirect('english:list_words')
        else:
            form = DeleteWord(instance=word)
    return {
        'form': form,
        'id': word_id
    }
