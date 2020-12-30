from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='objectives-home'),
    path('home/', views.home, name='objectives-home'),
    path('tasks/', views.tasks, name='objectives-tasks'),
    path('new_task', views.new_task, name='objectives-new-task'),
    path('update_task/<str:pk>/', views.update_task, name='objectives-update-task'),
    path('delete_task/<str:pk>/', views.delete_task, name='objectives-delete-task'),
    path('properties/', views.properties, name='objectives-properties'),
    path('new_property/', views.new_property, name='objectives-new-property'),
    path('update_property/<str:pk>/', views.update_property, name='objectives-update-property'),
    path('categories/', views.categories, name='objectives-categories'),
    path('new_category/', views.new_category, name='objectives-new-category'),
    path('update_category/<str:pk>/', views.update_category, name='objectives-update-category'),
    path('departments/', views.departments, name='objectives-departments'),
    path('new_department/', views.new_department, name='objectives-new-department'),
    path('update_department/<str:pk>/', views.update_department, name='objectives-update-department'),
    path('people/', views.people, name='objectives-people'),
    path('new_person/', views.new_person, name='objectives-new-person'),
    path('update_person/<str:pk>/', views.update_person, name='objectives-update-person'),
    path('statuses/', views.statuses, name='objectives-statuses'),
    path('new_status/', views.new_status, name='objectives-new-status'),
    path('update_status/<str:pk>/', views.update_status, name='objectives-update-status')
]
