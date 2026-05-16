from dotenv import load_dotenv
import os
from django.shortcuts import render
from django.views.generic import TemplateView
from .services import APIServiceDNIVehicular
from datetime import date, datetime
from django.utils.dateparse import parse_date

load_dotenv()

class DnivehicularIndexView(TemplateView):
    template_name = 'dnivehicular/resultado.html'

    def get_context_data(self, **kwargs):
        # Llamar al método padre para obtener el contexto base
        context = super().get_context_data(**kwargs)
        
        # Capturar el parámetro GET 'dni'
        dni = self.request.GET.get('dni')
        
        if dni and dni.isdigit() and len(dni) == 8:
            # Construir la URL con el DNI capturado
            base_url = os.getenv("API_CONSULTA_VEHICULAR") + dni
            api = APIServiceDNIVehicular(base_url=base_url)
            datos = api.consultar_dni_vehicular()
            #print(datos)
        else:
            # Si no hay DNI o no es válido, asignar None
            datos = None
        
        # Agregar los datos al contexto
        #print(datos)
        context['datos'] = datos
        context['hoy'] = date.today() # Formatear la fecha actual como 'YYYY-MM-DD'
        
        # if datos and 'Revalida' in datos and datos['Revalida']:
        #     try:
        #         revalida_date = datetime.strptime(datos['Revalida'], '%d/%m/%Y').date()
        #         context['estado'] = 'Vigente' if revalida_date >= context['hoy'] else 'Vencida'
        #     except ValueError:
        #         context['estado'] = 'Fecha de revalidación no válida'
        # else:
        #    context['estado'] = 'Fecha de revalidación no disponible'
        #print(type(datetime.strptime(datos['Revalida'], '%d/%m/%Y').date()))
        #print(context['hoy'])
        
        
        #diferencia = datetime.strptime(datos['Revalida'], '%d/%m/%Y').date() - context['hoy']
        #if diferencia.days <=0:
        #    context['estado'] = 'Vencida'
        #else:
        #    context['estado'] = 'Vigente'
        
        # Retornar el contexto actualizado
        return context