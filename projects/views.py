from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout
from users.models import bills


#def home (request):
#    return render(request, 'homePage.html')





def home(request):


    if request.user.is_authenticated:
        return render(request, 'homePage2.html')

    else:
    
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if request.user.is_authenticated:
             return render(request, 'landing.html') #message to let know user already authenticated
            if form.is_valid():
                user = form.get_user()
                login(request, user)
            else:
                return render(request, 'homePage.html', context={'form': form})
            return redirect('/users/landing')
        else:
            form = AuthenticationForm()
            return render(request, 'homePage.html', context={'form': form})



def contact(request):
    return render(request, 'contact.html')
 
 
def about(request):
    return render(request, 'about.html')
 
