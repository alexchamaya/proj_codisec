import logging

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm



# Create your views here.
def Contact_view(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            full_message = f"Mensaje de {name} <{email}>:\n\n{message}"
            logger = logging.getLogger(__name__)
            try:
                send_mail(
                    subject,
                    full_message,
                    settings.DEFAULT_FROM_EMAIL,
                    ['tecboxtechno@gmail.com']
                )
            except Exception as e:
                logger.exception('Error al enviar correo de contacto')
                if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                    return JsonResponse({"success": False, "message": "Error al enviar el correo."}, status=500)
                messages.error(request, 'Error al enviar el correo.')
                return redirect('contact')

            # Éxito: responder JSON si es AJAX, si no redirigir con message
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': 'Formulario enviado correctamente'})
            messages.success(request, 'Formulario enviado correctamente')
            return redirect('contact')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': form.errors}, status=400)
            # No-AJAX: mostrar errores en la misma página
            for field, errs in form.errors.items():
                messages.error(request, f"{field}: {', '.join(errs)}")
            return redirect('contact')

    # GET y otros métodos: mostrar el formulario
    form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})