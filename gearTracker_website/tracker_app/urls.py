from django.conf.urls import url
from . import views

app_name = 'tracker_app'
urlpatterns = [
    url(r'^$', views.index_view.Index.as_view(), name='index'),

    # Login
    url(r'^login/', views.login_view.Login.as_view(), name='login'),	
    url(r'^login_customer/', views.login_view.login_customer, name='login_customer'),	

    # Register
    url(r'^register/', views.register_view.Register.as_view(), name='register'),
    url(r'^register_customer/', views.register_view.register_customer, name='register_customer'),

    # Camera 
    url(r'^add-camera/', views.camera_model_view.CameraModelView.as_view() , name='camera'),
    url(r'^add-camera-make/', views.camera_make_view.CameraMakeView.as_view() , name='add-camera-make'),

    # Lens 
    url(r'^add-lens/', views.lens_model_view.LensModelView.as_view() , name='lens'),
    url(r'^add-lens-make/', views.lens_make_view.LensMakeView.as_view() , name='add-lens-make'),

    # Event
    url(r'^add-event/', views.event_view.EventView.as_view() , name='event'),
    url(r'^event-gear/', views.event_has_gear_view.EventHasGearView.as_view(), name='event_gear'),
    url(r'^photoshoot/', views.photoshoot_view.PhotoShootView.as_view(), name='photoshoot'),

    # Pack Gear
    url(r'^pack-gear/(?P<id>\d+)/$', views.pack_gear_view.PackGearView.as_view(), name='pack_gear'),
    
]
