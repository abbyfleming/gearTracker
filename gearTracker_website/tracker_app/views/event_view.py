from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect

from tracker_app.models import Event


class EventView(TemplateView):
    ''' 
    Purpose:
        Allow a user to create an event (ie: Wedding)

    get: 
        Returns all events
    
    post: 
        Create an event
    
    '''

    template_name = 'create_event.html'

    def get(self, request):

        self.all_events = Event.objects.all()

        return render(
            request, 'create_event.html',
            {'event': self.all_events,}
            )


    def post(self, request):
        data = request.POST

        name = data['event']

        create_event = Event.objects.create(
            name=name,
            )

        # Redirect to same page
        return HttpResponseRedirect("/event-gear")


    
    

  