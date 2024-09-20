from django.urls import path, include

from .views import APIRubricsViewSet


from rest_framework import routers

router = routers.DefaultRouter()

router.register('rubrics', viewset=APIRubricsViewSet)

urlpatterns = [
    path('api/', include(router.urls))
]