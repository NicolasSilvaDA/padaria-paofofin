from django.urls import path
from index.views import index_view


urlpatterns = [
    path('', index_view, name='index_page'),
]
