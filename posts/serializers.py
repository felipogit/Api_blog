from rest_framework import serializers
from .models import Post
from users.serializers import UserSerializer
import cloudinary.uploader
import cloudinary

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    img = serializers.SerializerMethodField()
    
    class Meta:
        model = Post
        fields = ['id', 'user', 'title', 'desc', 'img', 'cat', 'date']

    def get_img(self, obj):
        img_url = obj.img.url if obj.img else ""
        img_url = img_url.replace("http://localhost:8000", "")
        img_url = img_url.lstrip("/http%3A/")
        return img_url
