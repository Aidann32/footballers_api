from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
import django_filters.rest_framework

from core.views import BaseModelViewSet
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class PostViewSet(BaseModelViewSet):
    queryset = Post.objects.filter(is_active=True).order_by('created_at')
    serializer_class = PostSerializer

    def create(self, request, *args, **kwargs):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.validated_data['author'] = request.user
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

class CreateComment(generics.CreateAPIView):
    queryset = Comment.objects.filter(post__is_active=True)
    serializer_class = CommentSerializer

    

    