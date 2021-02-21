from django.urls import path, re_path
from django.conf.urls import url, include
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'levels', LevelViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'topics', TopicViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]