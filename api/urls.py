from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import *
from rest_framework import renderers
from api import views



user_list = UserViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

sensor_list = SensorViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
sensor_detail = SensorViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

territories_list = TerritoryViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
territories_detail = TerritoryViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = format_suffix_patterns([
    url(r'^$', api_root),
    url(r'^sensor/$', sensor_list, name='sensor-list'),
    url(r'^sensor/(?P<pk>[0-9]+)/$', sensor_detail, name='sensor-detail'),
    url(r'^users/$', user_list, name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail'),
    url(r'^territories/$', territories_list, name='territories-list'),
    url(r'^territories/(?P<pk>[0-9]+)/$', territories_detail, name='territories-detail')
])

# Login and logout views for the browsable API
urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]