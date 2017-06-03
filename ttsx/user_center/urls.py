from django.conf.urls import include, url
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register/', views.register),
    url(r'^register2/', views.register2),
    url(r'^is_registed/', views.is_registed),
    url(r'^login/', views.login),
    url(r'^login2/', views.login2),
    url(r'^user_center_info/', views.user_center_info),
    url(r'^user_center_order/', views.user_center_order),
    url(r'^user_center_site/', views.user_center_site),
    url(r'^user_center_site_submit/', views.user_center_site_submit),
    url(r'^quit/', views.quit),
]

