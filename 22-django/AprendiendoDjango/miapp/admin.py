from django.contrib import admin
from .models import Article, Category

# Configurar vista personalizada para Article
class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')

# Registrar modelos
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)

# Configurar títulos del panel de administración
admin.site.site_header = "Django ADSO - SENA"
admin.site.site_title = "Django ADSO - SENA"
admin.site.index_title = "Panel de Gestión"