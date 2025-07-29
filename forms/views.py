from django.shortcuts import render
from .forms import Form1
# Create your views here.
def home_view(request):
    return render(request,"home.html")
def contact_view(request):
    if request.method =='POST':
        form= Form1(request.POST)
        if form.is_valid():
            form.send_email()
            return render(request,"success.html",{"form":form})
        else:
            form=Form1()

    return render(request,"contact.html",{"form":form})

def success_view(request):
    return render(request,"success.html")