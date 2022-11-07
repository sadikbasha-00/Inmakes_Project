from django.urls import path, include
from todoapp import views

urlpatterns = [
    path('',views.add,name='add'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('clv/',views.TaskListview.as_view(),name='TaskListview'),
    path('cdv/<int:pk>/',views.TaskDetailview.as_view(),name='TaskDetailview'),
    path('cuv/<int:pk>/',views.TaskUpdateview.as_view(),name='TaskUpdateview'),
    path('cdelv/<int:pk>/',views.TaskDeleteview.as_view(),name='TaskDeleteview')
]
