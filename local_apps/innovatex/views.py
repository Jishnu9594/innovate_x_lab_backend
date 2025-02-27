from django.shortcuts import render
from .models import *
from .Serializers import*
from rest_framework import generics
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class ServiceList(generics.ListAPIView):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer

class ServiceDetail(generics.RetrieveAPIView):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = 'pk'  # Use 'pk' (UUID) as the lookup field

class ServiceCreate(generics.CreateAPIView):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer

class ServiceUpdate(generics.UpdateAPIView):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = 'pk'  # Use 'pk' (UUID) as the lookup field

class ServiceDelete(generics.DestroyAPIView):
    queryset = Services.objects.all()
    serializer_class = ServiceSerializer
    lookup_field = 'pk'  # Use 'pk' (UUID) as the lookup field

# List all clients (GET) and Create a new client (POST)
class ClientListCreateView(generics.ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

# Retrieve a single client (GET)
class ClientDetailView(generics.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'pk'  # Use 'pk' for UUID or primary key lookup

# Update a client (PUT or PATCH)
class ClientUpdateView(generics.UpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'pk'

# Delete a client (DELETE)
class ClientDeleteView(generics.DestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    lookup_field = 'pk'

# creation of projects
class CaseStudyCreate(generics.CreateAPIView):
    queryset = CaseStudy.objects.all()
    serializer_class = CaseStudySerializer
   

#listing of projects
class CaseStudyListing(generics.ListAPIView):
    queryset = CaseStudy.objects.all()
    serializer_class = CaseStudySerializer


#retrieve of projects
class CaseStudyRetrieve(generics.RetrieveAPIView):
    queryset = CaseStudy.objects.all()
    serializer_class = CaseStudySerializer
    lookup_field = "pk"


#updation of projects
class CaseStudyUpdate(generics.UpdateAPIView):
    queryset = CaseStudy.objects.all()
    serializer_class = CaseStudySerializer
    lookup_field = "pk"



#Deletion of projects
class CaseStudyDelete(generics.DestroyAPIView):
    queryset = CaseStudy.objects.all()
    serializer_class = CaseStudySerializer
    lookup_field = "pk"

class TestimonialsListView(generics.ListCreateAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer

    def get_serializer_context(self):
        return {"request": self.request}


# deatiled view of a testimonal
class TestimonialRetrieveAPIView(generics.RetrieveAPIView):
    queryset  = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    lookup_field = "pk"

# delation view of a testimonal
class TestimonialDeleteView(generics.DestroyAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer
    lookup_field = "pk"


class TeamListView(generics.ListCreateAPIView):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer

    def get_serializer_context(self):
        return {"request": self.request}  # Pass request context to serializer
    


class BlogListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def get_serializer_context(self):
        return {"request":self.request}
    

class JobPositionList(generics.ListAPIView):
    queryset = JobPosition.objects.all()
    serializer_class = JobPositionSerializer


class JobApplicationCreateView(generics.CreateAPIView):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer

    def perform_create(self, serializer):
        application = serializer.save()

        # Send an email confirmation
        send_mail(
            subject="Job Application Received",
            message=f"Dear {application.name},\n\nThank you for applying for {application.job}. We will review your application and get back to you soon.",
            from_email="jishnuaswin025@gmail.com",
            recipient_list=[application.email],
            fail_silently=False,
        )




class ContactMessageCreateView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            contact_message = serializer.save()

            # Send email notification
            send_mail(
                subject=f"New Contact Message: {contact_message.subject}",
                message=f"""
                Name: {contact_message.first_name} {contact_message.last_name}
                Email: {contact_message.email}
                Phone: {contact_message.phone}
                Subject: {contact_message.subject}
                Message: {contact_message.message}
                """,
                from_email="your_email@example.com",  # Replace with your email
                recipient_list=["admin@example.com"],  # Replace with recipient email
                fail_silently=False,
            )

            return Response({"message": "Message sent successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)