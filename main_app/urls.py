from django.urls import path 
from . import views 

# TODO: Update topics/
urlpatterns = [
    path('', views.home, name='home'),
    path('topics/create/', views.TopicCreate.as_view(), name='topics_create'),
    path('topics/', views.TopicIndex.as_view(), name='index'),
    path('topics/<int:topic_id>/update/', views.TopicUpdate.as_view(), name='topics_update'),
    path('topics/<int:topic_id>/delete/', views.TopicDelete.as_view(), name='topics_delete'),
    path('topics/<int:topic_id>/', views.topics_detail, name='detail'),
    path('topics/<int:topic_id>/create/', views.add_post, name='posts_create'),
    path('topics/<int:topic_id>/<int:post_id>/update/', views.PostUpdate.as_view(), name='posts_update'),
    path('topics/<int:topic_id>/<int:post_id>/delete/', views.PostDelete.as_view(), name='posts_delete'),
    path('topics/<int:topic_id>/<int:post_id>/', views.posts_detail, name='posts_detail'),
    path('topics/<int:topic_id>/<int:post_id>/create', views.add_comment, name='comments_create'),
    path('topics/<int:topic_id>/<int:post_id>/<int:comment_id>/update', views.CommentUpdate.as_view(), name='comments_update'),
    path('topics/<int:topic_id>/<int:post_id>/<int:comment_id>/delete', views.CommentDelete.as_view(), name='comments_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]