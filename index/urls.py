from django.urls import path
from index import views


urlpatterns = [
    path('', views.index_view, name='index_page'),
    
]
