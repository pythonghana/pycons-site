from django import template 

register = template.Library()
from registration.models import Profile


@register.inclusion_tag('2022/speakers/speakers_home.html')
def show_home_speaker():
    speaker_h_home = Profile.objects.filter(is_visible=True).order_by('date_created')
    return {'speaker_h_home': speaker_h_home}
