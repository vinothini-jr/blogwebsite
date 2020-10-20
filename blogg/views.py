from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post, Comment
from .forms import CommentForm, RegisterForm
from django.urls import reverse_lazy
# Create your views here.
class home(ListView):
    model = Post
    template_name = "blogg/home.html"

class details(DetailView):
    model = Post
    template_name = "blogg/detail.html"

class addcomments(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = "blogg/add_comments.html"
    #fields=("name","body")
    def form_valid(self, form):
        form.instance.post_id = self.kwargs["pk"]
        return super().form_valid(form)
    success_url = reverse_lazy('home')
class prof(DetailView):
    model = Post
    template_name = "blogg/profileinfo.html"

#class register_view(CreateView):
def register_view(request):
    form=RegisterForm(request.POST or None)
    if form.is_valid():
        form.save()
    context={
        "form":form
    }
    return render(request,'blogg/register.html',context)








