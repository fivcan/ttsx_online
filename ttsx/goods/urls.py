from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^index/$', views.index),
    url(r'^json_index/$', views.json_index),
    url(r'^detail/$', views.detail),
    url(r'^goods_more/$', views.goods_more),
]
