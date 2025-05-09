from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import EventsForm, GalleryForm, ResourcesForm, TeamForm, MapForm
from .models import Events, Farmersdata, Gallery,hhdata, Resources, Team, geomap
from django.http import HttpResponse, HttpResponseForbidden
##############################################################
# Create your views here.
def index_view(request):
    return render(request, 'index.html', {})

def home_view(request):
    return render(request, 'home.html', {})

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password= request.POST['password']
        user=authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('home')  # Default fallback view
        else:
            messages.success(request, 'There was an error in logged in ...!')
            return redirect('login')
    else:
        return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    return redirect('index')
###################################################################
def create_event_view(request):
    if request.method == 'POST':
        form = EventsForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.total_participants = event.male_participants + event.female_participants  # Ensure total is set
            event.save()
            return redirect('event_list')  # Update with the correct view name
            
    else:
        form = EventsForm()
    return render(request, 'create_event.html', {'form': form})

def edit_event_view(request, event_id):
    
        event = get_object_or_404(Events, event_id=event_id)
        if request.method == 'POST':
            form = EventsForm(request.POST, instance=event)
            if form.is_valid():
                form.save()
                return redirect('event_list')  # Redirect to the event list after editing
        else:
            form = EventsForm(instance=event)
        return render(request, 'create_event.html', {'form': form})

def delete_event_view(request, event_id):    
    event = get_object_or_404(Events, event_id=event_id)
    if request.method == 'POST':
        event.delete()
        return redirect('event_list')  # Redirect to the event list after deletion       


def event_list_view(request):
    user_groups = list(request.user.groups.values_list('name', flat=True))
    form = EventsForm(request.POST, request.FILES)
    
    
        
    events = Events.objects.all()
    return render(request, 'event_list.html', {'events': events,'form': form,'user_groups': user_groups})

def nav_event_view(request):
    form = EventsForm(request.POST, request.FILES)
    
    
        
    events = Events.objects.all()
    return render(request, 'nav_events.html', {'events': events,'form': form})
############################################################## 
def create_gallery(request):
    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gallery')  # Redirect to the event list after creation
    else:
        form = GalleryForm()
    return render(request, 'create_gallery.html', {'form': form})

def edit_gallery(request, gallery_id):
    
        gallery = get_object_or_404(Gallery, gallery_id=gallery_id)
        if request.method == 'POST':
            form = GalleryForm(request.POST, instance=gallery)
            if form.is_valid():
                form.save()
                return redirect('gallery')  # Redirect to the event list after editing
        else:
            form = GalleryForm(instance=gallery)
        return render(request, 'create_gallery.html', {'form': form})

def delete_gallery(request, gallery_id):    
    gallery = get_object_or_404(Gallery, gallery_id=gallery_id)
    if request.method == 'POST':
        gallery.delete()
        return redirect('gallery') 
    
    return HttpResponse("Invalid request", status=400)   # Redirect to the event list after deletion       


def gallery(request):
    form = GalleryForm(request.POST, request.FILES)
    
    
        
    gallery = Gallery.objects.all()
    return render(request, 'gallery.html', {'gallery': gallery,'form': form})

def nav_gallery(request):
   form = GalleryForm(request.POST, request.FILES)
    
    
   gallery = Gallery.objects.all()
   return render(request, 'nav_gallery.html', {'gallery': gallery,'form': form})
###########################################################

from django.db.models import Q
'''
In Django, Q is a class from django.db.models that allows
 you to create complex database
 queries using logical operators like AND (&), OR (|), and NOT(~).

 here we used | or if user is in either in wassan or apmas accept filter to take both groups into filter

'''

def farmers_data_view(request):
    filters = Q()  # Initialize an empty query filter

    if request.user.groups.filter(name="wassan").exists():
        filters |= Q(gender="male")  # Include data where ngo is 'wassan'

    if request.user.groups.filter(name="apmas").exists():
        filters |= Q(gender="female")  # Include data where ngo is 'apmas'

    if request.user.groups.filter(name="allngos").exists():
        farmers_data = Farmersdata.objects.all()  # If in 'allngos', show everything
    else:
        farmers_data = Farmersdata.objects.filter(filters)  # Apply the combined filter

    return render(request, 'farmers_data.html', {'farmers_data': farmers_data})

############################################################
def hhdata_list(request):
    # Fetch all hhdata records
    records = hhdata.objects.all()
    # Pass records to the template
    return render(request, 'farmers_data.html', {'records': records})
#####################################################
def create_map(request):
    if request.method == 'POST':
        form = MapForm(request.POST, request.FILES)
        if form.is_valid():
            
            
            form.save()
            return redirect('map')  # Update with the correct view name
            
    else:
        form = EventsForm()
    return render(request, 'create_map.html', {'form': form})

def edit_map(request, map_id):
    
        maps = get_object_or_404(geomap, map_id=map_id)
        if request.method == 'POST':
            form = MapForm(request.POST, instance=maps)
            if form.is_valid():
                form.save()
                return redirect('map')  # Redirect to the event list after editing
        else:
            form = EventsForm(instance=maps)
        return render(request, 'create_map.html', {'form': form})

def delete_map(request, map_id):    
    maps = get_object_or_404(geomap, map_id=map_id)
    if request.method == 'POST':
        maps.delete()
        return redirect('map')  # Redirect to the event list after deletion       


def map_list(request):
    user_groups = list(request.user.groups.values_list('name', flat=True))
    form = MapForm(request.POST, request.FILES)
    
    
        
    maps = geomap.objects.all()
    return render(request, 'map.html', {'maps': maps,'form': form,'user_groups': user_groups})

#nav_map section
from django.core.serializers import serialize
from django.http import HttpResponse
from django.http import JsonResponse




def map_view(request):
    return render(request, "nav_map.html")

def get_maps(request):
    maps = geomap.objects.all()
    data = [{
        "name": m.map_name,
        "url": m.geodata.url  # Returns URL like /media/maps/filename.geojson
    } for m in maps]
    return JsonResponse(data, safe=False)
