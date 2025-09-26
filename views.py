from django.shortcuts import render, redirect
from .models import Video, Usuario
from .forms import VideoForm, UsuarioForm

def videos_view(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('videos')
    else:
        form = VideoForm()
    videos = Video.objects.all()
    return render(request, 'videos.html', {'form': form, 'videos': videos})

def usuarios_view(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('usuarios')
    else:
        form = UsuarioForm()
    usuarios = Usuario.objects.all()
    return render(request, 'usuarios.html', {'form': form, 'usuarios': usuarios})

def creditos_view(request):
    return render(request, 'creditos.html')
