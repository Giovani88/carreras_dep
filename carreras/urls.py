from django.urls import path, include
from rest_framework import routers
from carreras import views

router = routers.DefaultRouter()
router.register('carreras',views.CarrerasView,'carreras')

urlpatterns = [
    path("api/v1/", include(router.urls))
]
