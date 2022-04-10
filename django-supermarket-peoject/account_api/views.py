from rest_framework import viewsets
from account_api.models import User
from account_api.serializers import UserSerializer, UserDetailSerializer
from account_api.permissions import IsSuperuser

class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    lookup_field = 'username'
    permission_classes = [IsSuperuser]
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update', 'retrieve']:
            return UserDetailSerializer
        return UserSerializer
 
    
