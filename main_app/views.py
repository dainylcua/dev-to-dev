from django.shortcuts import render, redirect
from .models import Post, Comment, Topic
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.utils import timezone

# TODO: Redirect succesful Post delete to the specific topic the post was from
# TODO: Redirect succesful Comment delete to the specific post the comment was from
# TODO: Add User and Post ID to comments
# TODO: Add User and Topic ID to posts
# Create your views here.
def home(request):
  return render(request, 'home.html')

class TopicIndex(ListView):
  model = Topic
  template_name = 'topics/index.html'

class TopicUpdate(UpdateView):
  model = Topic
  template_name = 'topics/index.html'

class TopicCreate(CreateView):
  model = Topic
  fields = ['title', 'subtitle']

class TopicDelete(DeleteView):
  model = Topic
  success_url = '/topics/'

def topics_detail(request, topic_id):
  topic = Topic.objects.get(id=topic_id)
  return render(request, 'topics/index.html', {
    'topic': topic
  })

# class PostIndex(ListView):
#   model = Post
#   template_name = 'posts/index.html'

class PostCreate(CreateView):
  model = Post
  fields = ['title', 'description']

class PostUpdate(UpdateView):
  model = Post
  fields = ['description']

class PostDelete(DeleteView):
  model = Post
  success_url = '/topics/'

def posts_detail(request, post_id):
  post = Post.objects.get(id=post_id)
  return render(request, 'topics/index.html', {
    'post': post
  })

# # Potentially remove this? We might only need post_show
# class CommentIndex(ListView):
#   model = Comment
#   template_name = 'posts/detail.html'

#  Potentially change to def add_comment? Similar to assoc_feeding in catcollector
class CommentCreate(CreateView):
  model = Comment
  fields = 'content'

class CommentUpdate(UpdateView):
  model = Comment
  fields = 'content'

class CommentDelete(DeleteView):
  model = Comment
  success_url = '/topics/'

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # Handles new user creation
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('home')
      # Creates a session entry in the database and persists it sitewide until logging out
    else:
      error_message = 'invalid data - please try again'

  else:
    # This is for GET requests, assuming our user clicked on "signup" from the navbar
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)