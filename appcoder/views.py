from django.contrib.auth.mixins import UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect, render
from django.views.generic import ListView, DeleteView, UpdateView, DetailView
from .models import Publicacion
from .forms import PublicacionForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import logout, login as auth_login
from django.urls import reverse
from django.contrib import messages

# Create your views here.

def is_superuser(user):
    return user.is_superuser

def inicio(request):
    return render(request, 'appcoder/index.html', {
        'es_superusuario': request.user.is_superuser
    })

def about_me_view(request):
    return render(request, 'appcoder/about.me.html')

def inicio_no_autenticado(request):
    return render(request, 'appcoder/inicio_no_autenticado.html')

def crear_publicacion(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PublicacionForm(request.POST, request.FILES)
            if form.is_valid():
                publicacion = form.save(commit=False)
                publicacion.creador = request.user
                publicacion.save()
                return redirect('publicacion_list')
        else:
            form = PublicacionForm()
        return render(request,'appcoder/crear_publicacion.html', {'form': form})
    else:
        login_url = reverse('login_view')
        messages.info(request, f"Tienes que iniciar sesion para crear una publicacion. Inicia sesion <a href='{login_url}'>aqui</a>.")
        return redirect('inicio_no_autenticado')

class PublicacionListView(ListView):
    model = Publicacion
    template_name = 'publicacion_list.html'
    context_object_name = 'publicaciones'

class PublicacionDetailView(DetailView):
    model = Publicacion
    template_name = 'appcoder/publicacion_detail.html'
    context_object_name = 'publicacion'

class PublicacionUpdateView(UserPassesTestMixin, UpdateView):
    model = Publicacion
    fields = ['titulo', 'subtitulo', 'contenido', 'imagen']
    template_name = 'appcoder/publicacion_view.html'
    success_url = reverse_lazy("/")

    def test_func(self):
        return self.request.user.is_superuser

class PublicacionDeleteView(UserPassesTestMixin, DeleteView):
    model = Publicacion
    template_name = 'appcoder/publicacion_confirm_delete.html'
    success_url = reverse_lazy('publicacion_list')

    def test_func(self):
        return self.request.user.is_superuser
    
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('/')
    else:
        form = AuthenticationForm()
    return render(request, 'appcoder/login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('/')
        else:
            form = UserCreationForm()
        return render(request, 'appcoder/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/')