from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register/', views.register),
    url(r'^register2/', views.register2),
]

