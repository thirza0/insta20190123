from rest_framework import viewsets
from .models import User,Relationship
from rest_framework.permissions import IsAdminUser,IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .permission import IsSelf
from rest_framework.decorators import action
from .serializers import UserSerializer, RelationshipSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # def get_follower(self):

    def get_serializer_class(self):
        serializer = super().get_serializer_class()
        if self.action =='follow':
            return RelationshipSerializer
        return serializer

    def get_permissions(self):
        if self.action == 'create':

            return []
        permissions = super().get_permissions()

        if self.action == 'destroy':
            permissions.append(IsAdminUser())

        if self.action == 'update':
            permissions.append(IsSelf())

        return permissions


    @action(['POST'],True)
    def follow(self, request, pk):
        to_user = self.get_object()
        from_user = request.user

        serializer = self.get_serializer(data={
            'to_user':to_user,
            'from_user':from_user,
            'is_agree':to_user.is_public
        })

        return Response({'status':'ok'})

class FollowerViewSet(viewsets.ModelViewSet):
    queryset = Relationship.objects.all()
    serializer_class = RelationshipSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_permissions(self):
        if self.action == 'create':

            return []
        permissions = super().get_permissions()

        if self.action == 'destroy':
            permissions.append(IsAdminUser())

        if self.action == 'update':
            permissions.append(IsSelf())

        return permissions
