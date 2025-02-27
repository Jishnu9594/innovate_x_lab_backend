from django.db import models
from local_apps.main.models import Main

# Create your models here.


# model for service section
class Services(Main):
    service_title = models.CharField(max_length=255,blank=True,null=True)
    description = models.TextField(blank=True,null=True)
    icon = models.CharField(max_length=255,blank=True,null=True)

    class Meta:
        ordering = ["-created_at", "-updated_at"]
        verbose_name = 'Services'
        verbose_name_plural = 'Service'


    def __str__(self):
        return  self.service_title
    

#model for client section


class Client(Main):
    client_name = models.CharField(max_length=255, blank=True, null=True)
    client_logo = models.ImageField(upload_to="client_logos/", blank=True, null=True)

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def __str__(self):
        return self.client_name

    

#model for projects section

class CaseStudy(Main):
    project_title = models.CharField(max_length=255,blank=True,null=True)
    project_description = models.TextField(blank=True,null=True)
    project_image = models.ImageField(upload_to="case_studies/",blank=True,null=True)  
    project_link = models.URLField()

    class Meta:
        ordering = ["-created_at", "-updated_at"]
        verbose_name = 'CaseStudy'
        verbose_name_plural = 'CaseStudies'

    def __str__(self):
        return self.project_title
    


# model for testimonial
class Testimonial(Main):
    name = models.CharField(max_length=255,blank=True,null=True)
    company = models.CharField(max_length=255,blank=True,null=True)
    feedback = models.TextField()
    image = models.ImageField(upload_to="testimonials/",blank=True,null=True)  

    class Meta:
        ordering = ["-created_at", "-updated_at"]
        verbose_name = 'Testimonial'
        verbose_name_plural = 'Testimonials'

    def __str__(self):
        return f"Testimonial from {self.name} ({self.company})"



# model for teammember creation
class TeamMember(Main):
    name = models.CharField(max_length=255,blank=True,null=True)
    position = models.CharField(max_length=255,blank=True,null=True)
    image = models.ImageField(upload_to="team_members/",blank=True,null=True)  
    twitter_link = models.URLField(max_length=255,blank=True,null=True)
    linkedin_link = models.URLField(max_length=255,blank=True,null=True)

    class Meta:
        ordering = ["-created_at", "-updated_at"]
        verbose_name = 'TeamMember'
        verbose_name_plural = 'TeamMembers'

    def __str__(self):
        return self.name



# model for Blog creation
class BlogPost(Main):
    blog_title = models.CharField(max_length=255,blank=True,null=True)
    excerpt = models.TextField(blank=True,null=True)
    image = models.ImageField(upload_to="blog_posts/",blank=True,null=True)
    link = models.URLField(max_length=255,blank=True,null=True)

    class Meta:
        ordering = ["-created_at", "-updated_at"]
        verbose_name = 'BlogPost'
        verbose_name_plural = 'BlogPosts'

    def __str__(self):
        return self.blog_title






class ContactMessage(Main):
    first_name = models.CharField(max_length=100,blank=True,null=True)
    last_name = models.CharField(max_length=100,blank=True,null=True)
    phone = models.CharField(max_length=20,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    subject = models.CharField(max_length=255,blank=True,null=True)
    message = models.TextField(blank=True,null=True)
    consent = models.BooleanField(blank=True,null=True)

    class Meta:
        ordering = ["-created_at", "-updated_at"]
        verbose_name = 'ContactMessage'
        verbose_name_plural = 'ContactMessages'

    def __str__(self):
        return f"Message from {self.first_name} {self.last_name} - {self.subject}"





class JobPosition(Main):
    title = models.CharField(max_length=255,blank=True,null=True)
    location = models.CharField(max_length=100,blank=True,null=True)
    posted_date = models.DateField(blank=True,null=True)
    deadline = models.DateField(blank=True,null=True)
    description = models.TextField(blank=True,null=True)

    class Meta:
        ordering = ["-posted_date"]
        verbose_name = 'JobPosition'
        verbose_name_plural = 'JobPositions'  # Show latest jobs first

    def __str__(self):
        return self.title




class JobApplication(Main):
    job = models.ForeignKey(JobPosition, on_delete=models.CASCADE, related_name="applications")
    name = models.CharField(max_length=255,blank=True,null=True)
    email = models.EmailField(blank=True,null=True)
    phone = models.CharField(max_length=255,blank=True,null=True)
    resume = models.FileField(upload_to="resumes/", blank=True, null=True)
    applied_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)


    class Meta:
        ordering = ["-created_at", "-updated_at"]
        verbose_name = 'JobApplication'
        verbose_name_plural = 'JobApplications'

    def __str__(self):
        job_title = self.job.title if self.job else "No Job Assigned"
        return f"{self.name} - {job_title}"
