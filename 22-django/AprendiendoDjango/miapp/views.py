from django.shortcuts import render, HttpResponse

# Create your views here.
# MVC = Modelo vista controlador -> Acciones (Metodos)
# MVT = Modelo template  vista ->  Acciones (Metodos)

layaut = """
<h1>Sitio WEB con Django | ADSO SENA </h1>
<hr/>
<ul>
    <li>
        <a herf = "/inicio"> Inicio </a>
    </li>
    <li>
        <a herf = "/hola-mundo">Hola mundo </a>
    </li>
    <li>
        <a herf = "/pagina-pruebas">Pagina pruebas </a>
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
    return HttpResponse(layaut+html)

def hola_mundo(request):
        return HttpResponse(layaut+"""
                                        <h1>Hola mundo con Django!!!</h1>
                                        <h3>Soy Aprendiz ADSO</h3>
                                        """)

def pagina(request):
        return HttpResponse(layaut+"""
                            <h1>Paguina de mi web</h1>
                            <p> Creado por ADSO Popayan</p> 
                            """)

def contacto(request, nombre, apellidos):
        return HttpResponse(layaut+f"<h2>Contacto {nombre} {apellidos}</h2>")