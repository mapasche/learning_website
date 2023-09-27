from django.shortcuts import render
from .models import Post
from django.utils import timezone

# Create your views here.
#Los viws son para conectar los models con los templates

def post_list (request):
    #lte -> less than or equal
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts' : posts})