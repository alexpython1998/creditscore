from. import views
from django.urls import path







urlpatterns = [

 path('', views.home, name='UCheck-Home'),
 path('registration/', views.registration, name='registration'),
 path('questions/', views.questions, name='questions'),
path('submit_polls/', views.submit_polls, name='submit_polls')
]