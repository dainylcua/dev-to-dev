from django.shortcuts import render, redirect
from .models import Post, Comment, Topic
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# TODO: Add User to comments
# TODO: Add User to posts
# Create your views here.
def home(request):
  return render(request, 'home.html')

class TopicIndex(ListView):
  model = Topic
  template_name = 'topics/index.html'

class TopicUpdate(LoginRequiredMixin, UpdateView):
  # Superuser required feature from django-braces
  def dispatch(self, request, *args, **kwargs):
    if not request.user.is_superuser:
      return redirect('/topics/')
    return super().dispatch(request, *args, **kwargs)
  
  model = Topic
  fields = ('title', 'subtitle',)

class TopicCreate(LoginRequiredMixin, CreateView):
  def dispatch(self, request, *args, **kwargs):
    if not request.user.is_superuser:
      return redirect('/topics/')
    return super().dispatch(request, *args, **kwargs)

  model = Topic
  fields = ['title', 'subtitle']

class TopicDelete(LoginRequiredMixin, DeleteView):
  def dispatch(self, request, *args, **kwargs):
    if not request.user.is_superuser:
      return redirect('/topics/')
    return super().dispatch(request, *args, **kwargs)

  model = Topic
  success_url = '/topics/'

def topics_detail(request, topic_id):
  topic = Topic.objects.get(id=topic_id)
  post_form = PostForm()
  return render(request, 'topics/detail.html', {
    'topic': topic,
    'post_form': post_form,
  })

@login_required
def add_post(request, topic_id):
  form = PostForm(request.POST)
  print(form._errors)
  if form.is_valid():
    new_post = form.save(commit=False)
    new_post.topic_id = topic_id
    new_post.user_id = request.user.id
    new_post.save()
  
  return redirect('detail', topic_id=topic_id)

class PostUpdate(LoginRequiredMixin, UpdateView):
  model = Post
  fields = ('description',)

class PostDelete(LoginRequiredMixin, DeleteView):
  model = Post

  def delete(self, *args, **kwargs):
    self.object = self.get_object()
    return super().delete(*args, **kwargs)

  def get_success_url(self):
    return reverse_lazy('detail', kwargs={'topic_id':self.object.topic.id})

def posts_detail(request, topic_id, post_id):
  post = Post.objects.get(id=post_id)
  topic_id = topic_id
  comment_form = CommentForm()
  return render(request, 'posts/detail.html', {
    'post': post,
    'comment_form': comment_form,
    'topic_id': topic_id
  })

@login_required
def add_comment(request, topic_id, post_id):
  form = CommentForm(request.POST)
  print(form._errors)
  if form.is_valid():
    new_comment = form.save(commit=False)
    new_comment.post_id = post_id
    new_comment.user_id = request.user.id
    new_comment.save()
  
  return redirect('posts_detail', topic_id=topic_id, post_id=post_id)


class CommentUpdate(LoginRequiredMixin, UpdateView):
  model = Comment
  fields = ('content',)

class CommentDelete(LoginRequiredMixin, DeleteView):
  model = Comment
  
  def delete(self, *args, **kwargs):
    self.object = self.get_object()
    return super().delete(*args, **kwargs)

  def get_success_url(self):
    return reverse_lazy('posts_detail', kwargs={'topic_id':self.object.post.topic.id, 'post_id': self.object.post.id})

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)