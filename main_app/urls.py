from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    # path('topics/', views.TopicIndex.as_view(), name='index'),
    # path('topics/<int:pk>/', views.topics_detail, name='detail'),
    # path('topics/create/', views.TopicCreate.as_view(), name='topics_create'),
    # path('topics/<int:pk>/update/', views.TopicUpdate.as_view(), name='topics_update'),
    # path('topics/<int:pk>/delete/', views.TopicDelete.as_view(), name='topics_delete'),
    # path('comments/', views.CommentList.as_view(), name='comments_index'),
    # path('comments/<int:pk>/', views.CommentDetail.as_view(), name='comments_detail'),
    # path('comments/create/', views.CommentCreate.as_view(), name='comments_create'),
    # path('comments/<int:pk>/update/', views.CommentUpdate.as_view(), name='comments_update'),
    # path('comments/<int:pk>/delete/', views.CommentDelete.as_view(), name='comments_delete'),
    # path('accounts/signup/', views.signup, name='signup'),
]