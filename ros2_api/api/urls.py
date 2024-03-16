# arquivo utilizado para definir as URL's da API
#!/usr/bin/env python
from django.contrib import admin
from django.urls import path, include, re_path

from .views import TopicView, ServiceView

urlpatterns = [
    re_path(r'topics/(?P<topic>[\w\-/]+)$', TopicView.as_view(), name='api_topics'),
    re_path(r'services/(?P<service>[\w\-/]+)$', ServiceView.as_view(), name='api_services'),

]