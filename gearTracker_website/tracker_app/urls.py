from django.conf.urls import url
from . import views

#url for each function which calls the view/function

app_name = 'tracker_app'
urlpatterns = [
    url(r'^$', views.index_view.Index.as_view(), name='index'),

    # Login
    url(r'^login/', views.login_view.Login.as_view(), name='login'),

    # Register
    url(r'^register/', views.register_view.Register.as_view(), name='register'),
    
]