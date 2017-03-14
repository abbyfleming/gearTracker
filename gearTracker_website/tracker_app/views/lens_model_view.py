from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect

from tracker_app.models import CameraMake
from tracker_app.models import CameraModel
from tracker_app.models import Customer


class LensModelView(TemplateView):
    """
    Purpose: Post and get Camera Models ie: D700, D750
    Methods: post, get
    Author: @abbyfleming
    """

    template_name = 'create_lens_model.html'

    def get(self, request):

        # Fetch the camera brands
        self.all_camera_makes = CameraMake.objects.all()

        return render(
            request, 'create_lens_model.html',
            {'camera_make': self.all_camera_makes,}
            )


    def post(self, request):
        data = request.POST

        # Fetch the data from the Form
        make = data['camera_list']
        model = data['camera_model']
        date = data['purchase_date']
    
        # Find the values of the FK
        customer_fk = Customer.objects.get(user=request.user.pk)     
        make_fk = CameraMake.objects.get(pk=make)

        # Create the camera model!
        create_camera_model = CameraModel.objects.create(
            customer=customer_fk,
            camera_model=make_fk,
            name=model,
            purchase_date=date,
            )

        # Redirect to same page
        return HttpResponseRedirect("/add-lens")


    
    

  