from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from posts.permissions import IsOwner
from .models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.parsers import MultiPartParser
import cloudinary.uploader


class PostCreateView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser]
    

    def perform_create(self, serializer):
        # Extrai a URL da imagem do resultado do Cloudinary e a salva no modelo
        result = cloudinary.uploader.upload(self.request.data.get('img'))
        serializer.save(user=self.request.user, img=result['url'])


   


class ListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class DestroyPostView(DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated,IsOwner]

class RetrievePostView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UpdatePostView(UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated,IsOwner]
    parser_classes = [MultiPartParser]

    def perform_update(self, serializer):
        result = cloudinary.uploader.upload(self.request.data.get('img'))
        serializer.save(user=self.request.user, img=result['url'])
    
