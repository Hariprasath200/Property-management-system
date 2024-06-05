
from django.shortcuts import render

from django.shortcuts import render
from .forms import LocationForm
from .models import Bus

def home(request):
    return render(request,'system/home.html')
def deposit(request):
    return render(request,'system/deposit.html')
def agent(request):
    return render(request,'system/agent.html')


from django.shortcuts import render, get_object_or_404
from .models import Bus, Location

from django.shortcuts import render
from .forms import LocationForm
from django.shortcuts import render, redirect, get_object_or_404
from .forms import LocationForm
from .models import Bus, Location

def bus(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            # Retrieve or create the from_location instance
            from_location_name = form.cleaned_data['from_location']
            from_location = get_object_or_404(Location, name=from_location_name)
            
            # Retrieve or create the to_location instance
            to_location_name = form.cleaned_data['to_location']
            to_location = get_object_or_404(Location, name=to_location_name)
            
            # Retrieve travel_date from the form data
            travel_date = form.cleaned_data['travel_date']
            
            # Check if a similar bus already exists in the database
            existing_bus = Bus.objects.filter(from_location=from_location, to_location=to_location, travel_date=travel_date).first()
            if not existing_bus:
                # Redirect to the search results page with the form data
                return redirect('search_results', from_location=from_location_name, to_location=to_location_name, travel_date=travel_date)
            else:
                # If similar bus exists, redirect to search results without creating a new bus
                return redirect('search_results', from_location=from_location_name, to_location=to_location_name, travel_date=travel_date)
    else:
        form = LocationForm()
    return render(request, 'system/bus.html', {'form': form})



from django.db.models import Q

from .models import Bus, Hotel, DepositCenter



def search_results(request, from_location, to_location, travel_date):
    # Retrieve buses, hotels, and deposit centers based on search criteria
    buses = Bus.objects.filter(from_location__name=from_location, to_location__name=to_location, travel_date=travel_date)
    
    # Assuming hotels and deposit centers can be located near both from_location and to_location
    hotels = Hotel.objects.filter(Q(location__name=from_location) | Q(location__name=to_location))
    deposit_centers = DepositCenter.objects.filter(Q(location__name=from_location) | Q(location__name=to_location))
    
    return render(request, 'system/search_results.html', {'buses': buses, 'hotels': hotels, 'deposit_centers': deposit_centers})
