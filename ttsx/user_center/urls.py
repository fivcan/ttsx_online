from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register/', views.register),
    url(r'^register2/', views.register2),
    url(r'^is_registed/', views.is_registed),
    url(r'^login/', views.login),
    url(r'^login2/', views.login2),
]

