from django.urls import path
from .views import *

urlpatterns = [
    
    # path('', post_list, name='post_list'),
    path('', render_post_list, name='post_list'),
    path('<int:id>/', post, name='post'),
    
    
    path('not-found/', not_found, name='not_found'),
]