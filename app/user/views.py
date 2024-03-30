# Combina operaciones CRUD, interactuar con los modelos
from rest_framework import viewsets
from app.user.models import User
from app.user.serializers import UserSerializer

class UserViewset(viewsets.ModelViewSet):
  # Conjunto de datos con el que va a trabajar
  queryset = User.objects.all() # Trabaje con todos los registros
  serializer_class = UserSerializer # Esqueleto
