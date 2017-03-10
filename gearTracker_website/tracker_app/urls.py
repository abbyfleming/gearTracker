from django.conf.urls import url
from . import views

#url for each function which calls the view/function

app_name = 'tracker_app'
urlpatterns = [
    url(r'^$', views.index_view.Index.as_view(), name='index'),

    # # Login
    # url(r'^customer_login/', views.login_view.login_customer, name='customer_login'),
    # url(r'^login/', views.login_view.Login.as_view(), name='login'),

    # # Register
    # url(r'^customer_register/', views.register_view.register_customer, name='customer_register'),
    # url(r'^register/', views.register_view.Register.as_view(), name='register'),
]