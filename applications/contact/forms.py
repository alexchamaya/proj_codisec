from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", max_length=100, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu Nombre', 'required': 'required'}))
    email = forms.EmailField(label="Correo Electrónico", required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Tu Email', 'required': 'required'}))
    subject = forms.CharField(label="Asunto", max_length=150, required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Asunto', 'required': 'required'}))
    message = forms.CharField(label="Mensaje", widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Tu Mensaje', 'required': 'required'}), required=True)
    