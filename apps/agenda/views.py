"""
    Script to crete CRUD of Agenda model.
"""
from django.shortcuts import render, get_object_or_404, redirect

from .models import Agenda
from .forms import AgendaForm

def index(request):
    return redirect('agenda')

def agenda_list(request):
    queryset: list = list(Agenda.objects.all().filter(
            contact_assign=request.user).exclude(is_active=False))
    context = {'agendas': queryset }
    return render(request=request, template_name='agenda/list.html', context=context)

def agenda_post(request):
    if request.method == "POST":
        form = AgendaForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.contact_assign = request.user
            contact.save()
            return redirect('agenda')
    form = AgendaForm()
    return render(request, 'agenda/edit.html', {'form': form, 'action': 'New'})

def agenda_detail(request, public_id):
    queryset = get_object_or_404(Agenda, public_id=public_id)
    return render(request=request, template_name='agenda/detail.html',
                    context={'agenda': queryset})

def agenda_update(request, public_id):
    queryset = get_object_or_404(Agenda, public_id=public_id)
    if request.method == "POST":
        form = AgendaForm(request.POST, instance=queryset)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.contact_assign = request.user
            contact.save()
            return redirect('agenda')
    form = AgendaForm(instance=queryset)
    return render(request=request, template_name='agenda/edit.html',
                    context={'form': form, 'action': 'Edit'})

def agenda_delete(request, public_id):
    queryset = get_object_or_404(Agenda, public_id=public_id)
    if request.method =="POST":
        queryset.is_active = False
        queryset.save()
        return redirect('agenda')
    return render(request, "agenda/delete.html", {'action': 'Delete'})
