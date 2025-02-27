from rest_framework import serializers
from .models import *


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = ['service_title', 'description', 'icon']




class ClientSerializer(serializers.ModelSerializer):
    client_logo = serializers.SerializerMethodField()

    class Meta:
        model = Client
        fields = ['client_name', 'client_logo']

    def get_client_logo(self, obj):
        request = self.context.get("request")
        if obj.client_logo:
            return request.build_absolute_uri(obj.client_logo.url)  # Full URL
        return None


class CaseStudySerializer(serializers.ModelSerializer):
    project_image = serializers.SerializerMethodField()

    class Meta:
        model = CaseStudy
        fields = ['project_title', 'project_description', 'project_image', 'project_link']

    def get_project_image(self, obj):
        request = self.context.get('request')
        if obj.project_image:
            image_url = obj.project_image.url  # Relative URL: /media/case_studies/image.jpg
            if request:
                return request.build_absolute_uri(image_url)  # Full URL: http://127.0.0.1:8000/media/case_studies/image.jpg
            return image_url  # Just return relative URL when request context is not available
        return None


class TestimonialSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Testimonial
        fields = ['name', 'company', 'feedback', 'image']

    def get_image(self, obj):
        request = self.context.get("request")
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None  # Return None if no image is present


class TeamMemberSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True) 
    class Meta:
        model = TeamMember
        fields = '__all__'



class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['blog_title', 'excerpt', 'image', 'link']

    def get_image(self, obj):
        request = self.context.get("request")
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None  # Return None if no image is present





class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['first_name', 'last_name', 'phone', 'email', 'subject', 'message', 'consent']



class JobPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobPosition
        fields = '__all__' 




class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = '__all__'