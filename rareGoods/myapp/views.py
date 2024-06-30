from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from myapp.models import Product, Category, Blog, Comment, Reply, Lokasi
from myapp.forms import CommentCreateForm, ProductCreateForm
from django.shortcuts import get_object_or_404

import folium

# Create your views here.
def index(request):
    return render(
        request,
        "index.html"
    )

def about(request):
    return render(
        request,
        "about.html"
    )

# diskusi
def dikusi_list(request):
    blogs = Blog.objects.all()
    return render(
        request, 
        "diskusi/diskusi-list.html",
        {"blogs" :  blogs}
    )

@login_required(login_url="auth/login")
def diskusi_detail(request, slug):
    blog = Blog.objects.get(slug=slug)
    recent_blogs = Blog.objects.order_by('-date')[:4]

    comments = Comment.objects.filter(blog=blog).order_by('date')

    for com in comments: 
        replies = Reply.objects.filter(parent_comment=com)
        print(f"Comment {com.id} has replies: {replies}")

    comment_len = Comment.objects.filter(blog=blog)

    if request.method == "POST":
        form = CommentCreateForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.blog = blog
            comment.save()
            return redirect("myapp:diskusi-detail", slug=blog.slug) 
    else:
        form = CommentCreateForm()

    return render(
        request, 
        "diskusi/diskusi-detail.html",
        {
            "blog" : blog,
            "recent_blogs" : recent_blogs,
            "comments" : comments,
            "comment_len" : comment_len,
            "form" : form,
            # "replies" : replies,
        }
    )

# product
def product_list(request):
    products = Product.objects.all()
    categorys = Category.objects.all()
    return render(
        request,
        "product/product-list.html",
        {
            "products" : products, 
            "categorys" : categorys
        }
    )

@login_required(login_url="auth/login")
def product_add(request):
    categorys = Category.objects.all()

    if request.method == "POST":
        form = ProductCreateForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)

            category_slug = request.POST["category"]
            product.category = get_object_or_404(Category, category_slug=category_slug)
            
            product.save()
            return redirect("myapp:products")
    else :
        form = ProductCreateForm()
    return render(
        request, 
        "product/product-add.html",
        {
            "categorys" : categorys,
            "form" : form
        }
    )

def product_detail(request, slug):
    product = Product.objects.get(slug=slug)

    return render(
        request,
        "product/product-detail.html",
        {"product" : product}
    )

def lokasi(request):
    locations = Lokasi.objects.all()

    # folium map
    m = folium.Map(location=[-7.007249284715008,110.34278739892912], zoom_start=13)

    # add marker
    for lokasi in locations:
        coordinates = (lokasi.latitude, lokasi.longitude)
        folium.Marker(coordinates, popup=lokasi.toko).add_to(m)

    return render(
        request,
        "lokasi/lokasi.html",
        {
            "map" : m._repr_html_(),
            "locations" : locations,
        }
    )
    
