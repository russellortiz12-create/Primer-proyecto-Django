from django import forms
from django.core import validators

class FormArticle(forms.Form):
    title = forms.CharField(
        label="Título",
        max_length=40,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Digite el título',
                'class': 'titulo_form_article'
            }
        ),
        validators=[
            validators.MinLengthValidator(4, 'El título es demasiado corto'),
            validators.RegexValidator('^[A-Za-z0-9ñÑáéíóúÁÉÍÓÚ ]*$', 'El título está mal formado', 'invalid_title')
        ]
    )

    content = forms.CharField(
        label="Contenido",
        widget=forms.Textarea,
        validators=[
            validators.MaxLengthValidator(500, 'El texto es demasiado largo')
        ]
    )

    public_options = [
        (1, 'Sí'),
        (0, 'No')
    ]

    public = forms.TypedChoiceField(
        label="¿Publicado?",
        choices=public_options
    )