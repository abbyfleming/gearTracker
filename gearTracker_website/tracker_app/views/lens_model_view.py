from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect

from tracker_app.models import LensMake
from tracker_app.models import LensModel
from tracker_app.models import Customer


class LensModelView(TemplateView):
    ''' 
    Purpose:
        Allow a user to create a lens model (ie: Nikon Nikkor 24-70 2.8)

    get: 
        Returns lens make, and lens
    
    post: 
        Create a lens
    
    '''

    template_name = 'create_lens_model.html'

    def get(self, request):

        # Fetch the lens brands
        all_lens_makes = LensMake.objects.all()
        customer_lens = LensModel.objects.filter(customer=request.user.pk)

        
        return render(request, self.template_name, {
            'lens_make': all_lens_makes,
            'customer_lens': customer_lens, 
            })


    def post(self, request):
        data = request.POST

        # Fetch the data from the Form
        make = data['lens_list']
        min_focal = data['min_focal']
        max_focal = data['max_focal']
        aperature = data['aperature']
    
        # Find the values of the FK
        customer = Customer.objects.get(user=request.user.pk) 
        lens = LensMake.objects.get(pk=make)


        # Create the lens!
        create_lens_model = LensModel.objects.create(
            customer = customer,
            lens_make = lens,
            min_focal_length = min_focal,
            max_focal_length = max_focal,
            aperature = aperature,
            )

        # Redirect to same page
        return HttpResponseRedirect("/add-lens")


    
    

  