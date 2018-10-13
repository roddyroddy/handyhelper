from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
    url(r'^$', views.index), #this is for display
    url(r'register$', views.register),
    url(r'login$', views.login),
    url(r'logoff$', views.logoff),
    url(r'dashboard$' , views.dashboard),
    url(r'addpage$', views.addpage),
    url(r'add$', views.add),
    url(r'delete/(?P<id>\d+)$', views.delete),
    url(r'view/(?P<id>\d+)$', views.view),
    url(r'editpage/(?P<id>\d+)$', views.editpage),
    url(r'update$', views.update),
    url(r'addmy/(?P<id>\d+)$', views.addmy),
    url(r'giveup/(?P<id>\d+)$', views.giveup)
]                            
