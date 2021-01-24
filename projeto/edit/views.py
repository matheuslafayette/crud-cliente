from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from .models import edit
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class editList(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = edit
    template_name='edit_list.html'
 

class editCreate(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = edit
    fields = {'nome', 'endereco', 'telefone', 'data_nascimento'}
    success_url = reverse_lazy('edit_list')

class editDelete(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = edit
    template_name = 'edit_confirm_delete.html'
    success_url = reverse_lazy('edit_list')

class editUpdate(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = edit
    fields = {'nome', 'endereco', 'telefone', 'data_nascimento'}
    template_name = 'edit_form.html'
    success_url = reverse_lazy('edit_list')



def login_user(request):
    return render(request, 'login.html')

@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home/')
        else:
            messages.error(request, 'Usuário/Senha inválidos.')
    return redirect('/login/')

@login_required(login_url='/login/')
def logout_user(request):
    logout(request)
    return redirect('/login')

@login_required(login_url='/login/')
def home(request):
    return render(request, 'home.html')




