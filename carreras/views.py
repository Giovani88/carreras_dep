from rest_framework import viewsets
from .serializer import CarrerasSerializer
from .models import Carreras

# Create your views here.
class CarrerasView(viewsets.ModelViewSet):
    serializer_class = CarrerasSerializer
    queryset = Carreras.objects.all()
