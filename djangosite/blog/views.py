from django.shortcuts import render

# Create your views here.

from .models import BlogPost

def blog_page_details_page(request):

    obj = BlogPost.objects.get(id=2)
    template_page='blog_page_details.html'
    context={'object':obj}
    return render(request,template_page,context)