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
    class Meta:
        model = CaseStudy
        fields = ['project_title', 'project_description', 'project_image', 'project_link']



class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = ['name', 'company', 'feedback', 'image']


class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = ['name', 'position', 'image', 'twitter_link', 'linkedin_link']



class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['blog_title', 'excerpt', 'image', 'link']




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