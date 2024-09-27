from django.views.generic import ListView
from django.shortcuts import render
from django.views import View
from pinlocations import settings

# Create your views here.

class HomeView(ListView):
    template_name = "mapAdminApp/home.html"
    context_object_name = 'mydata'
    success_url = "/"

class MapView(View): 
    template_name = "mapAdminApp/map.html"

    def get(self,request): 
        key = settings.GOOGLE_API_KEY
        #eligable_locations = Locations.objects.filter(place_id__isnull=False)
        eligable_locations = [
                                ["The Champions Sports Club", "Champions Clubhouse", "90210", "Beverly Hills", "USA", "123 Elm Street", 34.1030032, -118.4104684, "ChIJE9on3F3HwoAR9AhGJW_fL-I"],
                                ["Sunset Tennis Club", "Sunset Clubhouse", "10001", "New York", "USA", "456 Park Avenue", 40.712776, -74.005974, "ChIJOwg_06VPwokRYv534QaPC8g"],
                                ["Beach Volleyball Club", "Seaside Sports Center", "33139", "Miami Beach", "USA", "789 Ocean Drive", 25.7825453, -80.1340534, "ChIJyWEHuEmuEmsRm9hTkapTCrk"]
                            ]

        locations = []

        for a in eligable_locations: 
            data = {
                'lat': a[6], 
                'lng': a[7], 
                'name': a[0]
            }

            locations.append(data)


        context = {
            "key":key, 
            "locations": locations
        }

        return render(request, self.template_name, context)
