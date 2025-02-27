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
    path("case-studies/create/", CaseStudyCreate.as_view(), name="case-studies-create"),
    path("case-studies/list/", CaseStudyListing.as_view(), name="case-studies-list"),
    path("case-studies/<uuid:pk>/", CaseStudyRetrieve.as_view(), name="case-studies-detail"),
    path("case-studies/update/<uuid:pk>/", CaseStudyUpdate.as_view(), name="case-study-update"),
    path("case-studies/delete/<uuid:pk>/", CaseStudyDelete.as_view(), name="case-study-delete"),
    path("testimonials/", TestimonialsListView.as_view(), name="testimonials-list"),
    path("testimonials/<uuid:pk>/", TestimonialRetrieveAPIView.as_view(), name="testimonials-detail"),
    path("testimonials/delete/<uuid:pk>/", TestimonialDeleteView.as_view(), name="testimonials-delete"),
    path("teams/", TeamListView.as_view(), name="team-list"),
    path('blogs/', BlogListCreate.as_view(), name='blog-list'),
    path('jobs/', JobPositionList.as_view(), name='job-list'),
    path("apply/", JobApplicationCreateView.as_view(), name="apply-job"),
     path('contact/', ContactMessageCreateView.as_view(), name='contact-message'),





]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)