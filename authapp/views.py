from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def SignUpView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return alert("User created successfully!")  # Redirect to a success page
    else:
        form = UserCreationForm()
    return render(request,'authapp/signup.html', {'form': form})
            
        
