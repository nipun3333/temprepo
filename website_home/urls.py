from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('facilities_products', views.facilities_products, name="facilities_products"),

    path('contact_us', views.contact_us, name="contact_us"),
    path('about_us', views.about_us, name="about_us"),
    path('facilities_products/<str:cat>', views.products, name="products"),
    # path('condensers', views.condensers, name="condensers"),
    # path('tyre_recycling_plant', views.tyre_recycling_plant, name="tyre_recycling_plant"),
    # path('heat_exchangers', views.heat_exchangers, name="heat_exchangers"),
    # path('industrial_storage_tanks', views.industrial_storage_tanks, name="industrial_storage_tanks"),
    # path('pressure_vessels', views.pressure_vessels, name="pressure_vessels"),
    # path('chimeny', views.chimeny, name="chimeny"),
    # path('industrial_reactors', views.industrial_reactors, name="industrial_reactors"),
    # path('industrial_fabrication_service', views.industrial_fabrication_service, name="industrial_fabrication_service"),
]