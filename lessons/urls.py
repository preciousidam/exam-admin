from lessons.views.note import StudentNoteViewSet
from django.urls import path, re_path
from django.conf.urls import url, include
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register(r'lessons', LessonViewSet)
router.register(r'notes', AdminNoteViewSet)
router.register(r'personal-notes', StudentNoteViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]