from django.urls import path
from . import views

urlpatterns = [
    path('posts/create/',views.PostCreateView.as_view()), 
    path('posts/list/',views.ListView.as_view()),
    path('posts/<int:pk>/retrive/',views.RetrievePostView.as_view()),
    path('posts/<int:pk>/update/',views.UpdatePostView.as_view()),
    path('posts/<int:pk>/destroy/',views.DestroyPostView.as_view()),
]