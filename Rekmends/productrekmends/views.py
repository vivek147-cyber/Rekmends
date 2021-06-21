
import re
from django import forms
from django.db.models.fields import SlugField
from django.shortcuts import redirect, render
from .models import categories, Post, Review, Contact, Product, subscribeform
from .forms import Reviewfrom
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from math import ceil
from django.core.mail import send_mail

# Create your views here.


def nav(request):

    catblog = categories.objects.all()

    params = {
        'catblog': catblog,
    }

    return render(request, 'nav.html', params)


def footer(request):
    if request.method == 'GET':
        return render(request, 'footer.html')
    else:
        if request.method == 'POST':
            email = request.POST['email']
            subscribe = subscribeform(email=email)

            if len(subscribe.email) < 5:
                error_message = 'email must be 5 char long'

            error_message = None

        if not error_message:
            subscribe.save()
            send_mail(
                'Rekmends',
                'Thankyou for Subscribing',
                'from@example.com',
                [email],
                fail_silently=False,)

            return redirect('homepage')
        else:
            return render(request, 'footer.html', {'error': error_message})


def index(request):
    if request.method == 'GET':
        # trending
        post = Post.objects.all().order_by('-read')
        # latest
        latestpost = Post.objects.all().order_by('-created_at')

        products = Product.objects.all().order_by('-created_on')

        catblog = categories.objects.all()

        params = {
            'post': post,
            'latestpost': latestpost,
            'products': products,
            'catblog': catblog,
        }
        return render(request, 'index.html', params)
    else:
        if request.method == 'POST':
            email = request.POST['email']
            subscribe = subscribeform(email=email)

            if len(subscribe.email) < 5:
                error_message = 'email must be 5 char long'

            error_message = None

        if not error_message:
            subscribe.save()
            send_mail(
                'Rekmends',
                'Thankyou for Subscribing',
                'from@example.com',
                [email],
                fail_silently=False,)

            return redirect('homepage')
        else:
            return render(request, 'index.html', {'error': error_message})


def contact(request):

    catblog = categories.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact = Contact(name=name,
                          email=email,
                          message=message)

        contact.save()
        send_mail(
            'Rekmends',
            'Thankyou for Subscribing',
            'from@example.com',
            [email],
            fail_silently=False,)

    params = {
        'catblog': catblog,
    }

    return render(request, 'contact.html', params)


def about(request):
    catblog = categories.objects.all()
    params = {
        'catblog': catblog,
    }
    return render(request, 'about.html', params)


def category(request):

    catblog = categories.objects.all()
    categoryID = request.GET.get('category')
    # posts=Post.objects.all()

    if categoryID:
        prod = Post.get_all_product_by_category_id(categoryID)
        p = Product.get_all_product_by_category_name(categoryID)
    else:
        prod = Post.objects.all().order_by('-created_at')
        p = Product.objects.all().order_by('-created_on')

    # blogs pagination
    paginator = Paginator(prod, 3)
    page = request.GET.get('page')

    try:
        blogs = paginator.get_page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    # products pagination
    pag = Paginator(p, 3)
    pg = request.GET.get('page')

    try:
        products = pag.get_page(pg)
    except PageNotAnInteger:
        products = pag.page(1)
    except EmptyPage:
        products = pag.page(pag.num_pages)

    params = {}
    params['prod'] = blogs
    params['p'] = products
    params['catblog'] = catblog
    return render(request, 'category.html', params)


def search(request):
    catblog = categories.objects.all()
    query = request.GET.get('q')
    post = Post.objects.filter(Q(title__icontains=query) | Q(
        category__name__icontains=query) | Q(decription__icontains=query))
    product = Product.objects.filter(Q(name__icontains=query) | Q(
        category__name__icontains=query) | Q(description__icontains=query))

    params = {
        'post': post,
        'product': product,
        'catblog': catblog,

    }

    return render(request, 'search.html', params)


def blog(request):

    catblog = categories.objects.all()
    post = Post.objects.all().order_by('-created_at')
    trendpost = Post.objects.all().order_by('-read')
    paginator = Paginator(post, 3)
    page = request.GET.get('page')

    try:
        blogs = paginator.get_page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    params = {
        'post': blogs,
        'trendpost': trendpost,
        'catblog': catblog,

    }
    return render(request, 'blog.html', params)


def blogdesc(request, slug, id):

    catblog = categories.objects.all()

    blogdesc = Post.objects.filter(slug=slug, pk=id)

    blog = Post.objects.get(id=id)
    blog.read = blog.read + 1
    blog.save()

    p = Post.objects.all().order_by('-read')

    reviews = Review.objects.filter(post_id=id).order_by('-id')

    params = {
        'blogdesc': blogdesc[0],
        'reviews': reviews,
        'catblog': catblog,
        'p': p,
    }

    return render(request, 'blogdesc.html', params)


def submit_review(request, post_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = Reviewfrom(request.POST)
        if form.is_valid():
            data = Review()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.message = form.cleaned_data['message']
            data.post_id = post_id
            data.save()
            send_mail(
                'Rekmends',
                'Thankyou for Subscribing',
                'from@example.com',
                [data.email],
                fail_silently=False,)
            return redirect(url)


def products(request):
    p = Product.objects.all().order_by('-created_on')
    budget_friendly = Product.objects.all().order_by('-newprice')

    paginator = Paginator(p, 3)
    page = request.GET.get('page')

    try:
        pro = paginator.get_page(page)
    except PageNotAnInteger:
        pro = paginator.page(1)
    except EmptyPage:
        pro = paginator.page(paginator.num_pages)

    params = {
        'p': pro,
        'budget_friendly': budget_friendly,

    }

    return render(request, 'products.html', params)
