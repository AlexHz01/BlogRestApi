from django.urls import path
from .views import CategoryModelViewSet
from rest_framework.routers import DefaultRouter

router_categories = DefaultRouter()

router_categories.register(prefix='categories', basename='categories', viewset=CategoryModelViewSet)


