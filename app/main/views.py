from django.contrib.auth.models import User
from django.views.generic import ListView, TemplateView
from rest_framework import filters
from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet


from .models import Product
from .serializers import ProductSerializer, UserSerializer


# Create your views here.


class ProductView(ModelViewSet, ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'short_disc', 'full_disc']


class UserView(ModelViewSet, ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdminUser,)

