from django.urls import path,include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('services/', ServiceList.as_view(), name='service-list'),
    path('services/<uuid:pk>/', ServiceDetail.as_view(), name='service-detail'),  # Use 'uuid' for the primary key
    path('services/create/', ServiceCreate.as_view(), name='service-create'),
    path('services/<uuid:pk>/update/', ServiceUpdate.as_view(), name='service-update'),  # Use 'uuid' for the primary key
    path('services/<uuid:pk>/delete/', ServiceDelete.as_view(), name='service-delete'),  # Use 'uuid' for the primary key
    path("clients/", ClientListCreateView.as_view(), name="client-list"),
    path("clients/<uuid:pk>/", ClientDetailView.as_view(), name="client-detail"),  # Change to <uuid:pk> if using UUID
    path("clients/<uuid:pk>/update/", ClientUpdateView.as_view(), name="client-update"),
    path("clients/<uuid:pk>/delete/", ClientDeleteView.as_view(), name="client-delete"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)