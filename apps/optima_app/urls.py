from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^$', views.index),
    url(r'^results$', views.results),
    url(r'^my_account/(?P<user_id>\w+)$', views.show_account),
    url(r'^update_account/(?P<user_id>\w+)$', views.update_account)
]