from rest_framework import serializers
from posts.models import Post
from users.api.serializers import UserViewSerializer
from categories.api.serializer import CategorySerialzier


class PostSerializer(serializers.ModelSerializer):
    user = UserViewSerializer()
    category = CategorySerialzier()

    class Meta:
        model = Post
        fields = '__all__'