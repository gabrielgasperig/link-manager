from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from .models import Link
from .forms import LinkForm

def link_list(request):
    category = request.GET.get('category', '')  # Obtém a categoria da URL
    if category:
        links = Link.objects.filter(category=category)  # Filtra por categoria
    else:
        links = Link.objects.all()  # Se não houver filtro, exibe todos

    categories = Link.objects.values_list('category', flat=True).distinct()  # Lista de categorias únicas
    return render(request, 'link_list.html', {'links': links, 'categories': categories, 'selected_category': category})

def add_link(request):
    if request.method == 'POST':
        form = LinkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('link_list')
    else:
        form = LinkForm()
    return render(request, 'add_link.html', {'form': form})

def edit_link(request, pk):
    link = get_object_or_404(Link, pk=pk)
    if request.method == 'POST':
        form = LinkForm(request.POST, instance=link)
        if form.is_valid():
            form.save()
            return redirect('link_list')
    else:
        form = LinkForm(instance=link)
    return render(request, 'edit_link.html', {'form': form})

def delete_link(request, pk):
    link = get_object_or_404(Link, pk=pk)
    if request.method == 'POST':
        link.delete()
        return redirect('link_list')
    return render(request, 'delete_link.html', {'link': link})

def share_link(request, pk):
    link = get_object_or_404(Link, pk=pk)
    if request.method == 'POST':
        email = request.POST['email']
        send_mail(
            'Confira este link!',
            f'Aqui está um link interessante: {link.url}',
            'seuemail@exemplo.com',
            [email]
        )
        return redirect('link_list')
    return render(request, 'share_link.html', {'link': link})
