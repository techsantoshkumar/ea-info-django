from django.conf.urls import url
from crud import views

urlpatterns=[
    url(r'^hello$',views.homePage),

    url(r'^index$', views.index),
    url(r'^create$', views.create),
    url(r'^update$', views.update),
    url(r'^view$',views.view),
    url(r'^delete$',views.delete),
]