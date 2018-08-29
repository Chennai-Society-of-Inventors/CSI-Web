from django.conf.urls import url

from CSI_Web import views

app_name = 'CSI_Web'

urlpatterns = [
    url(r'^$', views.index, name='index')
]