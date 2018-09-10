from django.conf.urls import url

from CSI_Web import views

app_name = 'CSI_Web'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^submit_problem', views.submit_problem, name='submit_problem'),
    url(r'^submit_invention', views.submit_invention, name='submit_invention')
]