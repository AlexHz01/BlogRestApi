from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.models import User
from users.api.serializers import UserRegisterSerializer, UserViewSerializer, UserUpdateSerializer

class RegisterView(APIView):

    def post(self, request):
        serilizer = UserRegisterSerializer(data=request.data)
        if serilizer.is_valid(raise_exception=True):
            serilizer.save()
            return Response(serilizer.data, status=status.HTTP_201_CREATED)
        return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserView(APIView):
    permissions = [IsAuthenticated]

    def get(self, request):
        serializer = UserViewSerializer(request.user)
        return Response(serializer.data)

    def put (self, request):
        user = User.objects.get(id=request.user.id)
        serializer = UserUpdateSerializer(user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
