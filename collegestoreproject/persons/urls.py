from django.urls import path

from . import views

urlpatterns = [
    path('add/', views.person_create_view, name='person_add'),
    path('<int:pk>/', views.person_update_view, name='person_change'),
    path('ajax/load-courses/', views.load_courses, name='ajax_load_courses'), # AJAX
    path('confirmation', views.confirmation, name='confirmation'),
]
