from django.views.generic import TemplateView
from django.shortcuts import render
from django.views import View
from pinlocations import settings
from geopy.geocoders import Nominatim


# Create your views here.

class MapView(View): 
    template_name = "mapAdminApp/map.html"

    def get(self,request): 
        key = settings.GOOGLE_API_KEY

        countries = [
                        ["Details","Afghanistan"],
                        ["Details","Albania"],
                        ["Details","Argentina"],
                        ["Details","Australia"],
                        ["Details","Bangladesh"],
                        ["Details","Brazil"],
                        ["Details","Canada"],
                        ["Details","India"],
                        ["Details","Sri Lanka"],
                        ["Details","United Kingdom"]
                    ]
        eligable_locations = []
        
        geolocator = Nominatim(user_agent="temp")

        for country in countries:  
            eligable_location = []
            location = geolocator.geocode(country[1])
            eligable_location.append(country[0])
            eligable_location.append(location.latitude)
            eligable_location.append(location.longitude)
            eligable_locations.append(eligable_location)
            print((location.latitude, location.longitude))


        locations = []




        for a in eligable_locations: 
            data = {
                'lat': a[1], 
                'lng': a[2], 
                'details': a[0]
            }

            locations.append(data)


        context = {
            "key":key, 
            "locations": locations
        }

        return render(request, self.template_name, context)
