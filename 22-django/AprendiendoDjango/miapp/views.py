from django.shortcuts import render, HttpResponse, redirect
from miapp.models import Article
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

    try:
        articulo = Article.objects.get(title="Matrix", public=False)
        response = f"Articulo:<br/>{articulo.id}. {articulo.title} "
    except:
        response = "<h1>Artículo no encontrado</h1>"

    return HttpResponse(response)

def editar_articulo(request, id):
    articulo = Article.objects.get(pk=id)

    articulo.title = "Batman"
    articulo.content = "Pelicula del 2017"
    articulo.public = True

    articulo.save()

    return HttpResponse(f"Articulo {articulo.id} actualizado: <strong>{articulo.title}</strong> - <strong>{articulo.content}</strong>")

def articulos(request):
    
    articulos = Article.objects.all()
    
    return render(request, 'articulos.html', {
        'articulos': articulos
    })
    
def borrar_articulo(request, id):
    articulo = Article.objects.get(pk=id)
    articulo.delete()
    
    return redirect('articulos')
def save_article(request):
    if request.method == 'POST':
        title = request.POST['title']
        if len(title) < 5:
            return HttpResponse("<h2>El título es muy pequeño (mínimo 5 caracteres)</h2>")
        
        content = request.POST['content']
        public = request.POST['public']

        articulo = Article(
            title=title,
            content=content,
            public=public
        )
        articulo.save()
        return HttpResponse(f"Artículo creado: <strong>{articulo.title}</strong> - {articulo.content}")
    else:
        return HttpResponse("<h2>No se ha podido crear el artículo</h2>")

# Vista que carga la plantilla del formulario simple
def create_article(request):
    return render(request, 'create_article.html')