from django.urls import path
from myapp import views

app_name = "myapp"

urlpatterns = [
    path("", views.index, name="index"),
    path("about", views.about, name="about"),

    #products
    path("products", views.product_list, name="products"),
    path("product-add", views.product_add, name="product-add"),
    path("product/<slug>", views.product_detail, name="product-detail"),

    #diskusi
    path("diskusi", views.dikusi_list, name="diskusi"),
    path("diskusi/<slug>", views.diskusi_detail, name="diskusi-detail"),

    #lokasi
    path("lokasi", views.lokasi, name="lokasi"),

    #comment
    # path("new-comment/<slug>", views.add_comment, name="new-comment"),
]
