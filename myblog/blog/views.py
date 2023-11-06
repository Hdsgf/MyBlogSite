from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Post
from .form import CommentsForm
# Create your views here.

class PostView(View):
    '''отображение записей'''
    def get(self, request):
        posts = Post.objects.all() #обращаемся ко всем объектам класса Post
        return render(request, 'blog/blog.html', {'post_list': posts})
    
class PostDetail(View):
    '''отдельная страница записей'''
    def get(self, request, pk):
        post = Post.objects.get(id=pk) 
        return render(request, 'blog/blod_detail.html', {'post': post})


class AddComments(View):
    ''''добавление коментариев'''
    def post(self, request, pk):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.save()
        return redirect(f'/{pk}')

