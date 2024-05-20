from django.shortcuts import render
from .models import Post, Categoria
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator

def home(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True)
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset)
        ).distinct()
        
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'index.html', {'posts': posts})


def detallePost(request, slug):
    post = get_object_or_404(Post, slug = slug)
    return render(request, 'blog/post.html', {'detallePost': post})

def generales(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact = 'Generales'))
    
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset), estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Generales')
        ).distinct()
        
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'blog/generales.html', {'posts':posts})

def programacion(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get (nombre__iexact = 'Programacion'))
    
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset), estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Programacion')
        ).distinct()
        
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)   
    return render(request,'blog/programacion.html', {'posts': posts})


def tutoriales(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True, categoria = Categoria.objects.get(nombre__iexact = 'Tutoriales'))
    
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset), estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Tutoriales')
        ).distinct()
        
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)    
    return render(request,'blog/tutoriales.html', {'posts':posts})

def videojuegos(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado= True, categoria = Categoria.objects.get(nombre__iexact = 'Videojuegos'))
    
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset), estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Videojuegos')
        ).distinct()
        
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)    
    return render(request,'blog/videojuegos.html', {'posts':posts})

def tecnologia(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado= True, categoria = Categoria.objects.get
    (nombre__iexact = 'Tecnologia'))
    
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(descripcion__icontains = queryset), estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Tecnologia')
        ).distinct()
        
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request,'blog/tecnologia.html', {'posts':posts})

