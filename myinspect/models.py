from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} ({self.email})"


    

class Visitor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    email = models.EmailField()
    description = models.TextField()
    id_proof = models.ImageField(upload_to='id_proofs/', blank=True, null=True)
    date_time = models.DateTimeField(auto_now_add=True)  # ✅ Correct image upload path

    def __str__(self):
        return self.name