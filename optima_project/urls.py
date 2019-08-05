from django.conf.urls import url, include


urlpatterns = [
    url(r'^', include('apps.optima_app.urls')),
]
