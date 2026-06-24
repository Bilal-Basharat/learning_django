from django.urls import path
from django.contrib import admin
from .views import *

urlpatterns = [
    
    # path('', post_list, name='post_list'),
    path('', render_post_list, name='post_list'),
    path('<int:id>/', post, name='post'),
    
    path('set', set, name='post'),
    path('get', get, name='post'),
    
    path('form/', post_form, name='post_form'),
    
    path('thank-you/', thank_you, name='thank_you'),

    path('not-found/', not_found, name='not_found'),
    
    path('delete-cookie/', delete_cookie, name='delete_cookie'),
]

admin.site.site_header = 'Blog Admin'
admin.site.site_title = 'Blog Admin Portal'
admin.site.index_title = 'Welcome to Blog Admin Portal'