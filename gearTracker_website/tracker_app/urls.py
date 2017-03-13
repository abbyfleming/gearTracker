from django.conf.urls import url
from . import views

#url for each function which calls the view/function

app_name = 'tracker_app'
urlpatterns = [
    url(r'^$', views.index_view.Index.as_view(), name='index'),

    # Login
    url(r'^login/', views.login_view.Login.as_view(), name='login'),	
    url(r'^login_customer/', views.login_view.login_customer, name='login_customer'),	

    # Register
    url(r'^register/', views.register_view.Register.as_view(), name='register'),
    url(r'^register_customer/', views.register_view.register_customer, name='register_customer'),

    # Create Camera Brand
    url(r'^camera_brand/', views.camera_brand_view.CameraBrandView.as_view() , name='camera_brand'),
]