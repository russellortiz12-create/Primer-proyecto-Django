from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from miapp.models import Article, Category

# Create your views here.
# MVC = Modelo vista controlador -> Acciones (Metodos)
# MVT = Modelo template  vista ->  Acciones (Metodos)

layout = """
<h1>Sitio WEB con Django | ADSO SENA </h1>
<hr/>
<ul>
    <li>
        <a href =  "/inicio"> Inicio </a>
    </li>
    <li>
        <a href = "/hola-mundo">Hola mundo </a>
    </li>
    <li>
        <a href = "/pagina-pruebas">Pagina pruebas </a>
    </li>
    <li>
        <a href = "/contacto">contacto </a>
    </li>
</ul>
<hr/>

"""

def index(request):
    
    html = """
        <h1>Inicio</h1>
        <p> Años hasta el 2050: </p> 
        <ul>
    """
    year = 2024
    while year <= 2050:
        if year % 2 == 0:
            html += f"<li>{str(year)}</li>"
        year += 1

    html += "</ul>"

    nombre = 'Carlos Gomez 2'
    lenguajes = ['JavaScript', 'Python', 'PHP', '#C']

    return render(request, 'index.html', {
    'title': 'Inicio 2',
    'mi_variable': 'Soy un dato que esta en la vista',
    'nombre': nombre,
    'lenguajes': lenguajes,
})

def hola_mundo(request):
    return render(request, 'hola_mundo.html')

def pagina(request, redirigir = 0):
    if redirigir == 1:
        return redirect('/inicio/')
    
    return render(request, 'pagina.html')

def contacto(request, nombre="", apellidos=""):
    html = ""
    
    if nombre and apellidos:
        html += "<p>El nombre completo es:</p>"
        html += f"<h3>{nombre} {apellidos}</h3>"
        
    return HttpResponse(layout+f"<h2>Contacto</h2>"+html) 

def crear_articulo(request, title, content, public):
    articulo = Article(
        title=title,
        content=content,
        public=public
    )
    articulo.save()
    return HttpResponse(f"Articulo creado: <strong>{articulo.title}</strong>")

def articulo(request):
    articulos = Article.objects.all()
    return render(request, 'articulo.html', {'articulos': articulos})

def editar_articulo(request, id):
    articulo = get_object_or_404(Article, id=id)

    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        content = request.POST.get('content', '').strip()

        if title and content:
            articulo.title = title
            articulo.content = content
            articulo.public = request.POST.get('public') == 'on'
            articulo.save()
            return redirect('articulo')

        return render(request, 'editar_articulo.html', {
            'articulo': articulo,
            'error': 'El título y el contenido son obligatorios.',
        })

    return render(request, 'editar_articulo.html', {'articulo': articulo})
