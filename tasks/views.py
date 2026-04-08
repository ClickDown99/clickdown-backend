from django.shortcuts import render
from django.shortcuts import HttpResponse
from . import models
import httpx
from time import sleep
#from http import HTTPStatus
from .client_config import (transport, before_request,
                            prepare_logger, after_request)


"""         
#Estrutura que será usada em toda requisição externa: 
with httpx.Client(
    transport=transport,
    event_hooks={'request': [before_request], 'response': [after_request]},timeout=5) as client:
"""
def delay(request, delay):
    sleep(delay)
    return None

def example_of_view_with_external_request(request):
    try:
        with httpx.Client(
            transport=transport,
            event_hooks={'request': [before_request], 'response': [prepare_logger, after_request]},
            timeout=5    
        ) as client:
            response = client.get('http://127.0.0.1:8000/tasks/delay/10')
            response.raise_for_status()
            return HttpResponse(response.content)
    except httpx.ReadTimeout: #HTTPStatus.REQUEST_TIMEOUT
        return HttpResponse('Request Timeout, try again later')
    except Exception as exc: #HTTPStatus.INTERNAL_SERVER_ERROR
        return HttpResponse(f'Exception: {exc}')

def example_page_content(request):
    try:
        tasks=dict(models.Task.objects.all())
        context={'tasks':tasks}
        return render(request=request, template_name='tasks_page_content.html', context=context)
    except Exception as exc:
        return HttpResponse(f'HTTP Exception: {exc}. Try again later')
    