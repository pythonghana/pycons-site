from django.shortcuts import render,  get_object_or_404
from django.utils.timezone import now
from .models import *  
from .models import EventYear
from fin_aid.models import Fin_aid

def get_fin_aid_status(year):
    event_year = get_object_or_404(EventYear, year=year)
    fin_aids = Fin_aid.objects.filter(event_year=event_year).order_by('-date_created')
    fin_aid_status = []

    for fin_aid in fin_aids:
        status = {
            'is_open': fin_aid.is_form_open(),
            'is_closed': fin_aid.is_form_closed(),
            'not_open_yet': fin_aid.is_form_not_open_yet(),
            'form_status_message': fin_aid.get_form_status_message()
        }
        fin_aid_status.append(status)

    return fin_aid_status

def homepage(request):
    current_year = now().year
    upcoming_pycon_events = PyConEvent.objects.filter(start_date__gte=now()).exclude(year=current_year)
    pycon_africa_this_year = EventYear.objects.filter(year=current_year).first()
    fin_aid_status = get_fin_aid_status(current_year)
    
    context = {
        'upcoming_pycon_events': upcoming_pycon_events,
        'pycon_africa_this_year': pycon_africa_this_year,
        'current_year': current_year,
        'fin_aid_status': fin_aid_status,
    }
    
    return render(request, 'home/home.html', context)


def home_for_year(request, year):
    event_year = EventYear.objects.get(year=year)
    template_name = f"{event_year.template_path}"
    context = {
        # Your context data here
        'event_year': event_year,
    }
    return render(request, template_name, context)

 
 


def handler404(request, exception):
    return render(request, '404.html', locals())

 
