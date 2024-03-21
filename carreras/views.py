from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializer import CarrerasSerializer
from .models import Carreras
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class CarrerasView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = CarrerasSerializer
    queryset = Carreras.objects.all()
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_active=False
        instance.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
