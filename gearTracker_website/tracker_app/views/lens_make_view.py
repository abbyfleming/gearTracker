from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect

from tracker_app.models import LensMake


class LensMakeView(TemplateView):
    """
    Purpose: LENS MAKE: Tamron, Petzel...
    Methods: post, get
    Author: @abbyfleming
    """

    template_name = 'create_lens_make.html'

    def get(self, request):

        self.all_lens_make = LensMake.objects.all()

        return render(
            request, 'create_lens_make.html',
            {'lens_make': self.all_lens_make,}
            )



    def post(self, request):
        data = request.POST

        name = data['lens_make']

        create_lens_make = LensMake.objects.create(
            name=name,
            )

        # Redirect to same page
        return HttpResponseRedirect("/add-lens-make")


    
    

  