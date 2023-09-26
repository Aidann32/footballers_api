from rest_framework.serializers import ModelSerializer, SlugRelatedField, StringRelatedField

from .models import Post, Comment


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        exclude = ('id', )


class PostSerializer(ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    author = StringRelatedField()

    class Meta:        
        model = Post
        # fields = ['author', 'title', 'content', 'updated_at', 'created_at', 'comment_set']
        fields = '__all__'
        # read_only_fields = ('comment_set',)