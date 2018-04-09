from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
def signup_view(req) :
    form = UserCreationForm()
    return render(req,'accounts/singup.html',{'form':form})
# Create your views here.
