from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.create_note),
    path('notes/<int:pk>/', views.get_note_detail),
    path('notes/<int:pk>/update/', views.update_note),
    path('notes/<int:pk>/delete/', views.delete_note),
    path('notes/all/', views.get_all_notes),
    path('notes/search/', views.search_notes, name='search_notes'),
]
