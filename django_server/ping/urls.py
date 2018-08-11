from django.conf.urls import url
from django_server.ping import views

urlpatterns = [
    url(r'^$', views.Ping.as_view()),
]
