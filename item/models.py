from django.db import models
from django.conf import settings

class LostItem(models.Model):
    STATUS_CHOICES = [
        ('lost', 'Perdido'),
        ('found', 'Encontrado'),
        ('returned', 'Devolvido'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    lost_date = models.DateField()
    lost_location = models.CharField(max_length=255)
    reward = models.DecimalField(max_digits=8, decimal_places=2,)
    
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='lost')
    
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='lost_items'
    )
    
    found_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        related_name='found_items'
    )

    def __str__(self):
        return self.title
