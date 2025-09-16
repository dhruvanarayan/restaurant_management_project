from django.urls import path
from . import views

urlpatterns = [
    path('my-notes/', views.my_notes, name='my_notes'),
    path('add-note/', views.add_note, name='add_note'),
]
