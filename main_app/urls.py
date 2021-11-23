from django.urls import path 
from . import views 

# TODO: Update topics/
urlpatterns = [
    path('', views.home, name='home'),
    path('topics/', views.PostIndex.as_view(), name='index'),
    # path('topics/<int:topic_id>/', views.topics_detail, name='detail'),
    # path('topics/create/', views.TopicCreate.as_view(), name='topics_create'),
    # path('topics/<int:topic_id>/update/', views.TopicUpdate.as_view(), name='topics_update'),
    # path('topics/<int:topic_id>/delete/', views.TopicDelete.as_view(), name='topics_delete'),
    # path('topics/<int:topic_id>/create/'),
    # path('topics/<int:topic_id>/<int:post_id>/update/'),
    # path('topics/<int:topic_id>/<int:post_id>/delete/'),
    # path('topics/<int:topic_id>/<int:post_id>/'),
    # path('topics/<int:topic_id>/<int:post_id>/create'),
    # path('topics/<int:topic_id>/<int:post_id>/<int:comment_id>/update'),
    # path('topics/<int:topic_id>/<int:post_id>/<int:comment_id>/delete'),
    # path('accounts/signup/', views.signup, name='signup'),
]