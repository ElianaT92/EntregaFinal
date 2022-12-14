from django import forms

# Create your models here.

class CursoFormulario(forms.Form):
    curso=forms.CharField()
    inicio=forms.IntegerField()

class ProfesorFormulario(forms.Form):
    profesor=forms.CharField()
    asignatura=forms.CharField()

class EgresadosFormulario(forms.Form):
    egresado=forms.CharField()
    titulacion=forms.CharField()