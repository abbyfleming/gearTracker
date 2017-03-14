from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect

from tracker_app.models import CameraMake
from tracker_app.models import Customer


class CameraModelView(TemplateView):
    """
    Purpose: Post and get Camera Models
    Methods: post, get
    Author: @abbyfleming
    """

    template_name = 'create_camera.html'

    def get(self, request):

        # Fetch the camera brands
        self.all_camera_brands = CameraMake.objects.all()

        return render(
            request, 'create_camera.html',
            {'camera_brand': self.all_camera_brands,}

            )



    def post(self, request):
        data = request.POST

        print("*****data*****", data)
        
        brand = data['camera_list']
        model = data['camera_model']
        date = data['purchase_date']

        current_customer = Customer.objects.get(user=request.user.pk)

        print("*****current_customer*****", current_customer)
        
        create_camera_brand = CameraMake.objects.create(
            camera_brand_name=brand,
            camera_model=model,
            purchase_date=date,
            customer=current_customer,
            )

        # Redirect to same page
        return HttpResponseRedirect("/camera_brand")


    
    

  