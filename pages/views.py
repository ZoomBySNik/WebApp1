from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request)
    print(request.user)
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    context={
        "my_text":"любой текст",
        "my_number":88005553535,
        "my_list":["spam", "eggs", 1, 2, 3],
    }
    return render(request, "contact.html", context)

def about_view(request, *args, **kwargs):
    return render(request, "about.html", {})

def social_view(request, *args, **kwargs):
    return render(request, "social.html", {})