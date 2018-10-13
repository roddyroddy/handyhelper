from __future__ import unicode_literals
from django.db import models

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)

class Jobs(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    taken = models.BooleanField(default = False)
    saved_by = models.ManyToManyField(User,related_name="saved_jobs")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, related_name="user_job")

class MyJobs(models.Model):
    user = models.ForeignKey(User, related_name="user_myjob", null=True)
    jobs = models.ForeignKey(Jobs, related_name="owned_job", null=True)
    title = models.CharField(max_length=255, null=True)
    description = models.CharField(max_length=255, null=True)
    # saved_by = models.ManyToManyField(User,related_name="saved_jobs")
    category = models.CharField(max_length=255, null=True)
    location = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

