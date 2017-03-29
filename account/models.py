from django.db import models
from django.conf import settings

class Profile(models.Model):
    POST_DOCT = 'POST_DOCT'
    GRADUATE = 'GRADUATE'
    COURSE_CHOICE = (
        (POST_DOCT, 'Post doctorial researcher'),
        (GRADUATE, 'Graduate student'),
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    date_of_birth = models.DateTimeField(blank=True, null=True)
    school = models.CharField(max_length=150, blank=True, null=True)
    graduate = models.CharField(max_length=120, blank=True, null=True)
    nation = models.CharField(max_length=120, blank=True, null=True)
    keywords = models.CharField(max_length=120, blank=True, null=True)