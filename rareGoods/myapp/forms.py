from django.forms import ModelForm
from django import forms
from myapp.models import Comment, Product

class CommentCreateForm(ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
        widgets = {
            "content" : forms.Textarea(attrs=
                                        {"class" :"form-control",
                                         "required" : "required",
                                         "placeholder" : "Your Comment"})
        }

class ProductCreateForm(ModelForm):
    class Meta:
        model = Product
        fields = ["product_name", "description", "pembelian", "price", "image"]
        widgets = {
                    "product_name" : forms.TextInput(attrs= 
                                                {"class" : "flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background  placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2",
                                                "required" : "required",
                                                "placeholder" : "Tulis nama produk disini"}),
                    "description" : forms.Textarea(attrs=
                                                   {"class" : "flex min-h-[80px] max-h-[90px] w-full rounded-t-md border focus:outline-none px-3 py-2 text-sm",
                                                    "required" : "required",
                                                    "placeholder" : "Tulis deskripsi produk disini"}),
                    "pembelian" : forms.TextInput(attrs=
                                                  {"class" : "flex h-10 w-full rounded-md border border-input bg-background px-3 py-2 text-sm ring-offset-background  placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-2",
                                                   "required" : "required",
                                                   "placeholder" : "www.example.com"}),
                    "price" : forms.TextInput(attrs=
                                              {"class" : "flex h-10 w-full border-none outline-none rounded-md bg-background  px-2 py-2 text-sm placeholder:text-muted-foreground",
                                               "required" : "required",
                                               "placeholder" : "0.00"}),
                    "image" : forms.FileInput(attrs=
                                              {"class" : "hidden",
                                               "accept" : "image/png, image/jpeg"})
        }