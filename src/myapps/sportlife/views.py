from django.shortcuts import render, get_object_or_404
from .models import Action


def action_list(request):
    actions = Action.active.all()
    return render(request,
                  'sportlife/action/action_list.html',
                  {'actions': actions})


def action_detail(request, title):
    action = get_object_or_404(Action, slug=title, status='active')
    return render(request,
                  'sportlife/action/action_detail.html',
                  {'action': action}
                  )
