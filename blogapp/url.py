from django.urls import path
from blogapp.views import *
urlpatterns = [
    path('index/', IndexView.as_view(), name='index'),
    path('list/',ListView.as_view(),name='list'),
    path('detail/',DetailView.as_view(),name='detail'),
    path('404/',Test_404View.as_view(),name='404'),
    path('test/',test),
]