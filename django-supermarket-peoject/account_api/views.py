from rest_framework import viewsets
from account_api.models import User
from account_api.serializers import UserSerializer, UserDetailSerializer
from account_api.permissions import IsSuperuser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    lookup_field = 'username'
    #permission_classes = [IsSuperuser]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filter_fields = ['is_active', 'is_staff', 'is_superuser']
    search_fields = ['email', 'username', 'first_name', 'last_name']
    ordering_fields = ['username', 'date_joined']
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update', 'retrieve']:
            return UserDetailSerializer
        return UserSerializer
 
    
