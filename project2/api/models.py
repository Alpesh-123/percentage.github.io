from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    maths = models.DecimalField(max_digits=5, decimal_places=2)
    chemistry = models.DecimalField(max_digits=5, decimal_places=2)
    physics = models.DecimalField(max_digits=5, decimal_places=2)
    history = models.DecimalField(max_digits=5, decimal_places=2)
    literature = models.DecimalField(max_digits=5, decimal_places=2)
    
    def __str__(self):
        return self.name()
