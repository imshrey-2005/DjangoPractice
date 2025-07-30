from django.shortcuts import render, redirect
from .forms import ContactForm 
# Create your views here.
def home_view(request):
    return render(request,"forms/home.html")
def contact_view(request):
    if request.method =='POST':
        form= ContactForm(request.POST)
        if form.is_valid():
            form.send_email()
            return redirect("success")
    else:
        form = ContactForm()
    context = {
        "form": form  # Make sure your template renders this form
    }
    return render(request, "forms/contact.html", context)

def success_view(request):
    return render(request,"forms/success.html")