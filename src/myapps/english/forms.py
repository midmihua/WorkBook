# -*- coding: utf-8 -*-


from django.forms import ModelForm
from myapps.english.models import Words


class AddNewWord(ModelForm):

    class Meta:
        model = Words
        fields = ['word', 'translation', 'comment']


class EditWord(ModelForm):

    def __init__(self, *args, **kwargs):
        super(EditWord, self).__init__(*args, **kwargs)
        self.fields['word'].widget.attrs['readonly'] = True

    class Meta:
        model = Words
        fields = ['word', 'translation', 'comment']


class DeleteWord(ModelForm):

    def __init__(self, *args, **kwargs):
        super(DeleteWord, self).__init__(*args, **kwargs)
        # self.fields['pk'].widget.attrs['readonly'] = True
        self.fields['word'].widget.attrs['readonly'] = True

    class Meta:
        model = Words
        fields = ['id', 'word']
