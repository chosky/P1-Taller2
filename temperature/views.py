from django.shortcuts import render, HttpResponse

import requests

def temperature(request):
    #return render(request, "temperature/temperature.html")
    
    # Verifica si hay un parámetro value en la petición GET
    if 'value' in request.GET:
        value = request.GET['value']
        # Verifica si el value no esta vacio
        if value:
            # Crea el json para realizar la petición POST al Web Service
            args = {'type': 'C', 'value': value}
            response = requests.post('http://127.0.0.1:8000/temperature/', args)
            # Convierte la respuesta en JSON
            temperature_json = response.json()

    # Realiza una petición GET al Web Services
    response = requests.get('http://127.0.0.1:8000/temperature/')
    # Convierte la respuesta en JSON
    temperatures = response.json()
    # Rederiza la respuesta en el template measure
    return render(request, "temperature/temperature.html", {'temperatures': temperatures})
