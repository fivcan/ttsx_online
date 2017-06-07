from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.cart),
    url(r'^add/$', views.add),
    url(r'^get_count/$', views.get_count),
    url(r'^delete/$', views.delete),
    url(r'^update/$', views.update),
]
