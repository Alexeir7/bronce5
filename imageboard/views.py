from django.shortcuts import render
from imageboard.models import Post
from django.http import HttpResponse


# Create your views here.
def index(request):
    images_list = Post.objects.order_by('-date')

    context_dict = {'images': images_list}

    return render(request, 'imageboard/index.html', context=context_dict)
