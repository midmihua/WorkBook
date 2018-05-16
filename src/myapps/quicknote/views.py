from django.shortcuts import redirect, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

from myapps.decorators import render_to

from myapps.quicknote.models import QuickNote
from myapps.quicknote.forms import AddQuickNoteForm, EditQuickNoteForm, DeleteQuickNoteForm


@render_to('quicknote/pages/list.tpl')
def list_notes(request):

    # Search field implementation
    if (request.POST.get('search_word') is None) or (len(request.POST.get('search_word')) <= 0):
        notes = QuickNote.objects.all().order_by('create_date')
    else:
        notes = QuickNote.objects.filter(note__icontains=request.POST.get('search_word')).order_by('create_date')

    page = request.GET.get('page', 1)
    paginator = Paginator(notes, 30)

    try:
        list_of_words = paginator.page(page)
    except PageNotAnInteger:
        list_of_words = paginator.page(1)
    except EmptyPage:
        list_of_words = paginator.page(paginator.num_pages)

    return {
        'notes': notes
    }


@render_to('quicknote/pages/add.tpl')
@login_required()
def add_note(request):
    form = AddQuickNoteForm(request.POST, request.FILES)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('quicknote:list_notes')
        else:
            form = AddQuickNoteForm()
    return {
        'form': form
    }


@render_to('quicknote/pages/edit.tpl')
@login_required()
def edit_note(request, note_id):
    note = get_object_or_404(QuickNote, pk=note_id)
    form = EditQuickNoteForm(request.POST or None, request.FILES or None, instance=note)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('quicknote:list_notes')
        else:
            form = EditQuickNoteForm(instance=note)
    return {
        'form': form
    }


@render_to('quicknote/pages/delete.tpl')
@login_required()
def delete_note(request, note_id):
    note = get_object_or_404(QuickNote, pk=note_id)
    form = DeleteQuickNoteForm(request.POST or None, instance=note)
    if request.method == 'POST':
        if form.is_valid():
            note.delete()
            return redirect('quicknote:list_notes')
        else:
            form = DeleteQuickNoteForm(instance=note)
    return {
        'form': form,
        'id': note_id
    }
