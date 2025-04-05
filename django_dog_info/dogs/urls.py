from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'breeds', views.BreedsViewSet)
router.register(r'dogs', views.DogsViewSet)

urlpatterns = [
    path('api/', include(router.urls))
]
