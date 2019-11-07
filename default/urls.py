from django.urls import path
from .views import *

urlpatterns = [
    #path('poll/', views.poll_list),
    path('', PollList.as_view()),
    path('<int:pk>/', PollDetail.as_view()),
    path('vote/<int:oid>/', PollVote.as_view()), 
    path('create/', PollCreate.as_view()), 
    path('<int:pk>/update/', PollUpdate.as_view()),
]
