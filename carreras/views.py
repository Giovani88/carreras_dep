from rest_framework import viewsets
from .serializer import CarrerasSerializer
from .models import Carreras
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class CarrerasView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CarrerasSerializer
    queryset = Carreras.objects.all()
