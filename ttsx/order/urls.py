from django.conf.urls import include, url
import views

urlpatterns = [
    url('^$', views.order),
    url('^create_order/$', views.create_order),
]