from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect

from tracker_app.models import CameraMake
from tracker_app.models import CameraModel
from tracker_app.models import Customer


class CameraModelView(TemplateView):
    ''' 
    Purpose:
        Allow a user to create a camera model. (ie: Nikon D700)

    get: 
        Returns camera_make and the customer's cameras
    
    post: 
        Create a camera model     
    '''

    template_name = 'create_camera_model.html'

    def get(self, request):

        # Fetch the camera brands
        self.all_camera_makes = CameraMake.objects.all()
        self.customer_camera = CameraModel.objects.filter(customer=request.user.pk)

        return render(
            request, 'create_camera_model.html', {
            'camera_make': self.all_camera_makes,
            'customer_camera': self.customer_camera,
            })


    def post(self, request):
        data = request.POST


        # Fetch the data from the Form
        make = data['camera_list']
        model = data['camera_model']
    
        # Find the values of the FK
        customer = Customer.objects.get(user=request.user.pk)     
        make = CameraMake.objects.get(pk=make)

        # Create the camera model!
        create_camera_model = CameraModel.objects.create(
            customer = customer,
            camera_make = make,
            name = model,
            )

        # Redirect to same page
        return HttpResponseRedirect("/add-camera")


    
    

  