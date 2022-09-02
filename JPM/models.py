from django.db import models
from django.utils import timezone


class Technology(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name




class GStack(models.Model):
    name = models.CharField(max_length=255)
    p = models.FloatField(default=0.0)

    def __str__(self):
        return self.name


class BlackBall(models.Model):
    name = models.CharField(max_length=255)
    title = models.BooleanField(default=False)
    word = models.BooleanField(default=False)
    tech = models.BooleanField(default=True)
     
    def __str__(self):
        return self.name


class JobPost(models.Model):
    title = models.CharField(max_length=1000, null=True)
    url = models.URLField(null=True)
    company_name = models.CharField(max_length=1000, null=True)
    job_type = models.CharField(max_length=1000, null=True)
    location = models.CharField(max_length=1000, null=True)
    posted_on = models.CharField(max_length=1000, null=True)
    qualification = models.CharField(max_length=1000, null=True)
    content = models.TextField(null=True)
    descriptors = models.CharField(max_length=1000, null=True)
    technologies = models.ManyToManyField(Technology, related_name="job_postings")
    cp = models.FloatField(default=0.0)
    bgc = models.BooleanField(default=False)
    garbage = models.BooleanField(default=False)
    same_state = models.BooleanField(default=False)

    downloaded = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

    class Meta:
        ordering = ('cp',)



days_choices = (
    ('1','Last 1 Day'),
    ('2','Last 3 Days')
)


class HLF(models.Model):
    filter_name = models.CharField(max_length=255)
    filter_url = models.CharField(max_length=1000)
    days = models.CharField(max_length=255, choices=days_choices, default='1')
