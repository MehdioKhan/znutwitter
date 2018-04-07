from django.urls import re_path
from . import views
urlpatterns= [
    re_path(r'^$',views.index,name='home'),
    re_path(r'^accounts/signup/$',views.signup,name='signup'),
    re_path(r'^(?P<username>\w+)$',views.profile,name='profile'),
]