
from django import forms
from django.db.models.fields import SlugField
from django.shortcuts import redirect, render
from .models import categories , Post,Review,Contact
from .forms import Reviewfrom
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
# Create your views here.

def index(request):
    post=Post.objects.all().order_by('-read')[:2]

    
    

    params={
        'post':post,
    }
    return render(request,'index.html',params)

def contact(request):
     if request.method=='POST':
       name=request.POST.get('name')
       email=request.POST.get('email')
       message=request.POST.get('message')

       

       contact = Contact(name=name,
                            email=email,
                           message=message)
      
       contact.save()

    
     return render(request,'contact.html')


def about(request):
    return render(request, 'about.html')


def category(request):

    catblog=categories.objects.all()
    categoryID=request.GET.get('category')
    #posts=Post.objects.all()

    if categoryID:
        prod=Post.get_all_product_by_category_id(categoryID)
    else:
        prod=Post.objects.all()

    params={}
    params['prod']=prod
    #params['posts']=posts
    params['catblog']=catblog
    return render(request, 'category.html',params)


def search(request):
    query = request.GET.get('q')
    post=Post.objects.filter( Q(title__icontains=query) | Q(category__name__icontains=query) | Q(decription__icontains=query))
    
    params={
        'post':post,
       
    }

    return render(request,'search.html',params)


def blog(request):


    post=Post.objects.all().order_by('-created_at')
    paginator = Paginator(post, 6)
    page = request.GET.get('page')

    try:
        blogs = paginator.get_page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    
    

    params={
        'post':blogs,
       
    }
    return render(request, 'blog.html',params)

def blogdesc(request,slug,id):

     

    blogdesc = Post.objects.filter(slug=slug, pk=id)

    blog=Post.objects.get(id=id)
    blog.read=blog.read + 1
    blog.save()

    reviews = Review.objects.filter(post_id=id)

    params={
        'blogdesc':blogdesc[0],
        'reviews':reviews
    }

    return render(request,'blogdesc.html',params)


def submit_review(request, post_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = Reviewfrom(request.POST)
        if form.is_valid():
            data = Review()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.message=form.cleaned_data['message']
            data.post_id = post_id
            data.save()
            return redirect(url)
