from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import EventsForm
from .models import Events, Farmersdata
from django.http import HttpResponse, HttpResponseForbidden

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

def create_event_view(request):
    if request.method == 'POST':
        form = EventsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')  # Redirect to the event list after creation
    else:
        form = EventsForm()
    return render(request, 'create_event.html', {'form': form})

def event_list_view(request):
    
    
        
    events = Events.objects.all()
    return render(request, 'event_list.html', {'events': events})
   
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


def edit_event_view(request, event_id):
    if request.user.has_perm('test_app.edit_events'):
        event = get_object_or_404(Events, event_id=event_id)
        if request.method == 'POST':
            form = EventsForm(request.POST, instance=event)
            if form.is_valid():
                form.save()
                return redirect('event_list')  # Redirect to the event list after editing
        else:
            form = EventsForm(instance=event)
        return render(request, 'create_event.html', {'form': form})
    
    else:
        # Return a forbidden response if the user lacks permissions or is not in the group
        return HttpResponseForbidden("You do not have the required permissions to edit this page.")

def delete_event_view(request, event_id):
    if request.user.has_perm('test_app.delete_events'):
        event = get_object_or_404(Events, event_id=event_id)
        if request.method == 'POST':
            event.delete()
            return redirect('event_list')  # Redirect to the event list after deletion        
    else:
        # Return a forbidden response if the user lacks permissions or is not in the group
        return HttpResponseForbidden("You do not have the required permissions to edit this page.")

        
    
