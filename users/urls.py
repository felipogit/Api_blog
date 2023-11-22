from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import MyTokenObtainPairSerializer

urlpatterns = [
    path('users/',views.UserCreate.as_view()),
    path('login/',TokenObtainPairView.as_view(serializer_class=MyTokenObtainPairSerializer), name='token_obtain_pair',) 
]