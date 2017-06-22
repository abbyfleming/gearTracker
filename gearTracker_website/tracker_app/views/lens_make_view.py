from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect

from tracker_app.models import LensMake


class LensMakeView(TemplateView):
    ''' 
    Purpose:
        Allow a user to create a lens make (ie: Sigma)

    get: 
        Returns all lens make
    
    post: 
        Create a lens make
    
    '''

    template_name = 'create_lens_make.html'

    def get(self, request):

        all_lens_make = LensMake.objects.all()
        
        return render(request, self.template_name, {
            'lens_make': all_lens_make,
            })



    def post(self, request):
        data = request.POST

        name = data['lens_make']

        create_lens_make = LensMake.objects.create(
            name=name,
            )

        # Redirect to same page
        return HttpResponseRedirect("/add-lens")


    
    

  