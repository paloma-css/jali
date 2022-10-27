from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Resenha
from .forms import ResenhaForm

# Create your views here.

def lista_resenhas(request):
    resenhas = Resenha.objects.filter(data_publicacao__lte=timezone.now()).order_by('data_publicacao')
    busca = request.GET.get('busca')
    if busca:
        resenhas = Resenha.objects.filter(titulo__icontains=busca)
    return render(request, 'home/lista_resenhas.html', {'resenhas': resenhas})

def detalhe_resenha(request, pk):
    resenha = get_object_or_404(Resenha, pk=pk)
    return render(request, 'home/detalhe_resenha.html', {'resenha': resenha})

def nova_resenha(request):
     if request.method == "POST":
         form = ResenhaForm(request.POST)
         if form.is_valid():
             resenha = form.save(commit=False)
             resenha.autor = request.user
             resenha.data_publicacao = timezone.now()
             resenha.save()
             return redirect('detalhe_resenha', pk=resenha.pk)
     else:
         form = ResenhaForm()
     return render(request, 'home/nova_resenha.html', {'form': form})

def editar_resenha(request, pk):
     resenha = get_object_or_404(Resenha, pk=pk)
     if request.method == "POST":
         form = ResenhaForm(request.POST, instance=resenha)
         if form.is_valid():
             resenha = form.save(commit=False)
             resenha.autor = request.user
             resenha.data_publicacao = timezone.now()
             resenha.save()
             return redirect('detalhe_resenha', pk=resenha.pk)
     else:
         form = ResenhaForm(instance=resenha)
     return render(request, 'home/nova_resenha.html', {'form': form})