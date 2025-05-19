from django.urls import path
from platforms import views

urlpatterns = [
    path('platforms/', views.PlatformListView.as_view(), name='platform-create-list'),
    path('platforms/<int:pk>/', views.PlatformRetrieveUpdateDestroyView.as_view(), name='platform-detail'),

]
