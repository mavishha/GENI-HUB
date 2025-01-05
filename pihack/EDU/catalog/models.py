from django.db import models # type: ignore
from django.contrib.auth.models import User # type: ignore

# Model for Study Plan
class catalog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Reference to the user
    study_type = models.CharField(max_length=100)
    hours_per_day = models.PositiveIntegerField()
    start_time = models.TimeField()
    num_subjects = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.study_type} - {self.user.username}"

# Model for Subject under Study Plan
class Subject(models.Model):
    study_plan = models.ForeignKey(catalog, on_delete=models.CASCADE, related_name='subjects')
    subject_name = models.CharField(max_length=100)  # Name of the subject
    section_video_url = models.URLField(blank=True, null=True)  # URL for the section video
    notes_upload = models.FileField(upload_to='notes/', blank=True, null=True)  # Uploads for notes

    def __str__(self):
        return self.subject_name
