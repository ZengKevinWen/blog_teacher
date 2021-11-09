from django.urls import path
from user.views import *
urlpatterns = [
    path('login/',LoginView.as_view(),name='login'),
    path('register/',RegisterView.as_view(),name='register'),
    path('SmsSDK/',Sent_Mess.as_view(),name='SmsSDK'),
]