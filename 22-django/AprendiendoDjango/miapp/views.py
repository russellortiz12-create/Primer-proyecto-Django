from django.shortcuts import render, HttpResponse

# Create your views here.
# MVC = Modelo vista controlador -> Acciones (Metodos)
# MVT = Modelo template  vista ->  Acciones (Metodos)

def index(request):
    
    html = """
        <h1>Inicio</h1>
        <p> Años hasta el 2050: </p> 
        <ul>
    """
    year = 2024
    while year <= 2050:
        html += f"<li>{str(year)}</li>"
        year += 1

    html += "</ul>"
    return HttpResponse(html)

def hola_mundo(request):
    return HttpResponse("""
        <h1>Hola mundo con Django!!!</h1>
        <h3>Soy Aprendiz ADSO</h3>
    """)

def paguina(request):
    return HttpResponse("""
                        <h1>Paguina de mi web</h1>
                        <p> Creado por ADSO Popayan</p> 
                        """)