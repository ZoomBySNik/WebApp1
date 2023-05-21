"""WebApp1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin, auth
from django.urls import path, re_path, include
from pages import views
from products.views import product_detail_view, LoanedBooksAllListView, registration
from products.views import product_detail_1_view, product_edit_view
from products.views import product_create_view, index_view, CompanyView, product_delete_view, LoanedBooksByUserListView

urlpatterns = [
    path('admin/', admin.site.urls),

    #path('', views.home_view, name='home_pages'),

    path('', index_view, name='home_pages'),

    path('contacts/', views.contact_view),

    path('about/', views.about_view),

    path('social/', views.social_view),

    path('detail/', product_detail_view, name='product_detail'),

    path('detail_product/<int:id>', product_detail_1_view),

    path('create/', product_create_view),

    path('product_delete/<int:id>', product_delete_view, name='delete_product'),

    path('product_edit/<int:id>', product_edit_view, name='edit_product'),

    re_path('company_list/', CompanyView.as_view(), name='company'),

    path('accounts/', include('django.contrib.auth.urls')),

    path('registration/', registration),

    re_path('borrowed/', LoanedBooksByUserListView.as_view(), name='my-borrowed'),

    re_path('all_borrowed/', LoanedBooksAllListView.as_view(), name='all-borrowed')
]
