from django.db import models

class Flashcard(models.Model):
    front_text = models.CharField(max_length = 150)
    back_text = models.CharField(max_length = 150)
    created_at = models.DateTimeField(auto_now=True)
    

# Create your models here.
