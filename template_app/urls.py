from django.urls import path
from django.conf.urls import url
from template_app import views

app_name = 'template_app'

urlpatterns = [
    url(r'^relative/$', views.relatives, name='relative'),
    url(r'^other/$', views.other, name='other'),
    url(r'^register/$', views.register, name='register'),
    path('', views.index, name='index')
]

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('other', views.other, name='other'),
#     path('relatives', views.relatives, name='relatives'),
# ]
