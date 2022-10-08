from django.shortcuts import render
from home.models import Contact

# Create your views here.

# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def post(request):
    return render(request, 'post.html')
def contact(request):
    if request.method=="POST":
         name=request.POST.get("name")
         email=request.POST.get("email")
         text=request.POST.get("text")
         number=request.POST.get("number")
         em = Contact( name=name, email=email, text=text, number=number)
         em.save()
    return render(request, 'contact.html')
def home1(request):
    return render(request, 'home1.html')