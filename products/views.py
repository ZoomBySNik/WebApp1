from django.shortcuts import render, redirect
from .models import Product,Company,ProductInstance
from .forms import ProductForm
from django.urls import  reverse
from django.views import generic
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from products.forms import RegistrationForm
# Create your views here.
def product_detail_view(request):
    obj = Product.objects.all()

    context = {
        "my_obj" : obj,
    }
    return render(request, "product/detail.html", context)

def product_detail_1_view(request, id):
    obj_1 = Product.objects.get(id=id)

    context = {
        "my_obj_1" : obj_1,
    }
    return render(request, "product/detail_product.html", context)

def product_create_view (request):
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            Product.objects.create(**form.cleaned_data)
    form = ProductForm()
    context = {
        "form" : form,
    }
    return render(request, "product/product_create.html", context)

def index_view(request):
    num_product = Product.objects.all().count()
    num_company = Company.objects.all().count()
    num_instance = ProductInstance.objects.all().count()
    num_instance_avalible = ProductInstance.objects.filter(status_id__exact=2).count()
    context = {
        'num_product':num_product,
        'num_company':num_company,
        'num_instance':num_instance,
        'num_instance_avalible':num_instance_avalible,
    }
    return render(request, 'home.html', context)

def product_delete_view(request, id):
    obj_2 = Product.objects.get(id=id)
    obj_2.delete()
    return  redirect(reverse('product_detail'))

def product_edit_view(request, id):
    get_product = Product.objects.get(id=id)
    if request.method == 'POST':
        get_product.title = request.POST.get('title')
        get_product.description = request.POST.get('description')
        get_product.weight = request.POST.get('weight')
        get_product.save()
        return HttpResponseRedirect('/detail')
    else:
        return render(request, "product/edit_product.html", {'get_product':get_product})

def registration(request):
    data = {}
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user=form.save(commit=False)
            new_user.save()
            data['form'] = form
            return render(request, 'registration/registration_out.html', data)
    else:
        form = RegistrationForm()
        data['form'] = form
    return render(request, 'registration/registration.html', data)
class CompanyView(generic.ListView):
    model=Company

class LoanedBooksByUserListView(LoginRequiredMixin, generic.ListView):
    model = ProductInstance
    template_name='product/bookinstance_list_custumer_user.html'
    paginate_by=10

    def get_queryset(self):
        return ProductInstance.objects.filter(custumer=self.request.user).filter(status_id__exact=3).order_by('due_back')

class LoanedBooksAllListView(generic.ListView):
    model = ProductInstance
    template_name='product/bookinstance_list_borrowed_all.html'
    context_object_name = 'productinstance_list'

    def get_queryset(self):
        return ProductInstance.objects.filter(status_id__exact=3).order_by('-due_back')