from pages.models import Page

def get_pages(request):
    pages = Page.objects.filter(visible=True) 

    return {
        'pages': pages
    } 
    
    