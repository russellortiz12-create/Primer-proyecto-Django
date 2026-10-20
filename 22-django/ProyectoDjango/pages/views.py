from django.shortcuts import render, get_object_or_404
from .models import Page

def page(request, slug):
    # Buscamos la página por su slug y que esté visible
    page = get_object_or_404(Page, slug=slug, visible=True)

    return render(request, 'pages/page.html', {
        'page': page
    })