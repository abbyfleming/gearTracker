from django.views.generic.base import TemplateView
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.http import HttpResponseRedirect

from tracker_app.models import LensModel
from tracker_app.models import Customer


class ListGearView(TemplateView):
    ''' 
    Purpose:
        Allow a user to see all of their gear including missing

    get: 
        Returns lens, missing lens
    
    post: 
        Updates gear from missing to found
    
    '''

    template_name = 'list_gear.html'

    def get(self, request):

        #LENS // REFACTOR
        all_lens = LensModel.objects.filter(customer=request.user.pk).filter(missing=False)

        #MISSING
        missing_lens = LensModel.objects.filter(customer=request.user.pk).filter(missing=True)

        return render(request, self.template_name, {
            'lens': all_lens,
            'missing_lens': missing_lens,
            })



    def post(self, request):
       
        lens = request.POST.getlist('lens')
    
        # LENS
        all_lens = LensModel.objects.filter(customer=request.user.pk).filter(missing=False)

        #MISSING
        missing_lens = LensModel.objects.filter(customer=request.user.pk).filter(missing=True)
    
        #Update gear to found and safe   
        for l in lens:
            pack_lens = LensModel.objects.filter(pk=l).update(missing=False, safely_packed=True)

        return render(request, self.template_name, {
            'lens': all_lens,
            'missing_lens': missing_lens,
            })






    
    

  