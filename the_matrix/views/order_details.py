import googlemaps
import json
from django.conf import settings
from django.shortcuts import render

def geocode(request):
    gmaps = googlemaps.Client(key= settings.GOOGLE_API_KEY)
    result = json.dumps(gmaps.geocode(str('Stadionstraat 5, 4815 NC Breda')))
    result2 = json.loads(result)
    latitude = result2[0]['geometry']['location']['lat']
    longitude = result2[0]['geometry']['location']['lng']
    context = {
        'result':result,
        'latitude':latitude,
        'longitude':longitude
    }
    return render(request, 'main_app/driver_order.html', context)