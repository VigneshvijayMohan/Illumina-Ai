from django.db import models

class UploadedFile(models.Model):
    original_filename = models.CharField(max_length=255)
    unique_filename = models.CharField(max_length=255, unique=True)
    file_hash = models.CharField(max_length=64, unique=True)  # SHA-256 hash
    file_path = models.CharField(max_length=500)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.original_filename