from django.shortcuts import render, HttpResponse

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
    return render(request, 'index.html')

def hola_mundo(request):
    return render(request, 'hola_mundo.html')

def pagina(request, redirigir = 0):
    if redirigir == 1:
        return redirect('/inicio/')
    
    return render(request, 'pagina.html')

def contacto(request, nombre="", apellidos=""):
        html = ""
        if  nombre and apellidos:
            html += "<p>El nombre completo es: </p>"
            html += f"<h3>{nombre} {apellidos}</h3>"
        return HttpResponse(layout+f"<h2>Contacto </h2>"+html)