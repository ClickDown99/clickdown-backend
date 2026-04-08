from django.urls import path#, include
from . import views

urlpatterns = [
    path('', views.example_page_content, name='example_page_content'),
    path('external-request/', views.example_of_view_with_external_request,
        name='example_of_view_with_external_request'),
]