from django.shortcuts import render
from django.http import HttpResponse
from test_app.form import UserForm

# Create your views here.
def add_user(request):
    form = UserForm()
    return render(request, 'test_app/user_form.html', {'t_form': form})

