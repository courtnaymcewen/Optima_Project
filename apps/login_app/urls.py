from django.conf.urls import url 
from . import views

urlpatterns = [
    url(r'^login$', views.show_login),
    url(r'^success$', views.success),
    url(r'^add_user$', views.add_user),
    url(r'^process_login$', views.process_login),
    url(r'^logout$', views.logout),
]