from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.task,name='task'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cdvtask/',views.TaskListView.as_view(),name ='cdvtask'),
    path('cdvdetail/<int:pk>/',views.TaskDetailView.as_view(),name ='cdvdetail'),
    path('cdvupdate/<int:pk>/',views.TaskUpdateView.as_view(),name ='cdvupdate'),
    path('cdvdelete/<int:pk>/',views.TaskDeleteView.as_view(),name ='cdvdelete'),
]
