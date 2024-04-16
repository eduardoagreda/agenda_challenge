from django.urls import path

from apps.agenda.views import index, agenda_list, agenda_post, agenda_detail, agenda_update, agenda_delete

urlpatterns = [
    path('', index, name='index'),
    path('agenda/', agenda_list, name="agenda"),
    path('agenda/new', agenda_post, name="agenda_new"),
    path('agenda/<uuid:public_id>', agenda_detail, name="agenda_detail"),
    path('agenda/<uuid:public_id>/edit', agenda_update, name='agenda_edit'),
    path('agenda/<uuid:public_id>/delete', agenda_delete, name='agenda_delete'),
]
