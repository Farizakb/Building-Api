from rest_framework import serializers

from api.serializer import UserSerializer
from .models import Article

class ArticleSerializer(serializers.ModelSerializer):
    author = UserSerializer(source='user', read_only=True)
    class Meta:
        model = Article
        fields = [
            'pk',
            'author',
            'title',
            'body',
            'path',
            'endpoint',
        ]