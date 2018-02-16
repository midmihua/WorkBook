from django.forms import ModelForm
from myapps.quicknote.models import QuickNote


class AddQuickNoteForm(ModelForm):

    class Meta:
        model = QuickNote
        fields = ['note', 'file']


class EditQuickNoteForm(ModelForm):

    class Meta:
        model = QuickNote
        fields = ['note', 'file']


class DeleteQuickNoteForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(DeleteQuickNoteForm, self).__init__(*args, **kwargs)
        self.fields['note'].widget.attrs['readonly'] = True

    class Meta:
        model = QuickNote
        fields = ['id', 'note']
