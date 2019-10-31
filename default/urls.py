from django.urls import path
from . import views

urlpatterns = [
    #path('poll/', views.poll_list),
    path('poll/', views.PollList.as_view()),
    path('poll/<int:pk>/', views.PollDetail.as_view()),
]
