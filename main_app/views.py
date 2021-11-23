from django.shortcuts import render, redirect
from .models import Post, Comment, Topic
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import PostForm, CommentForm

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
  post_form = PostForm()
  return render(request, 'topics/detail.html', {
    'topic': topic,
    'post_form': post_form,
  })

# class PostIndex(ListView):
#   model = Post
#   template_name = 'posts/index.html'

# class PostCreate(CreateView):
#   model = Post
#   fields = ['title', 'description']

def add_post(request, topic_id):
  form = PostForm(request.POST)
  print(form._errors)
  if form.is_valid():
    new_post = form.save(commit=False)
    new_post.topic_id = topic_id
    new_post.save()
  
  return redirect('detail', topic_id=topic_id)

class PostUpdate(UpdateView):
  model = Post
  fields = ['description']

class PostDelete(DeleteView):
  model = Post
  success_url = '/topics/'

def posts_detail(request, topic_id, post_id):
  post = Post.objects.get(id=post_id)
  topic_id = topic_id
  comment_form = CommentForm()
  return render(request, 'posts/detail.html', {
    'post': post,
    'comment_form': comment_form,
    'topic_id': topic_id
  })

# # Potentially remove this? We might only need post_show
# class CommentIndex(ListView):
#   model = Comment
#   template_name = 'posts/detail.html'

#  Potentially change to def add_comment? Similar to assoc_feeding in catcollector
# class CommentCreate(CreateView):
#   model = Comment
#   fields = 'content'

def add_comment(request, topic_id, post_id):
  form = CommentForm(request.POST)
  print(form._errors)
  if form.is_valid():
    new_comment = form.save(commit=False)
    new_comment.post_id = post_id
    new_comment.save()
  
  return redirect('posts_detail', topic_id=topic_id, post_id=post_id)


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