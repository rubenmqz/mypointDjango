from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.reverse import reverse

from blog.models import Post


class BlogSerializer(serializers.ModelSerializer):
    title = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ("first_name", "username", "title", "url")


    def get_title(self, obj):
        return "Blog de {0} {1}".format(obj.first_name, obj.last_name)

    def get_url(self, obj):
        return reverse('blog_posts_by_user', args=[obj.username], request=self.context['request'])


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ("title", "imgURL", "summary", "publish_at")


class FullPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'