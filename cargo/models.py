from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
Status = (
    ("Sending_Shipment", "Sending_Shipment"),
    ("On_the_move", "On_the_move"),
    ("On_site", "On_site"),
    ("Received", "Received"),
)




def generate_custom_id():
    return str(uuid.uuid4())[:8]  # Generate a unique ID and truncate to 8 characters


class Sender(models.Model):
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    name    = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city    = models.CharField(max_length=100)
    email   = models.EmailField()
    phone   = models.CharField(max_length=15)
    status  = models.CharField(max_length=20, choices=Status, default="Sending_Shipment")
    percent = models.CharField(max_length=3 , default=0)
    
    def __str__(self):
        return f'{ self.user} submitted a request to be sent , Status is : {self.status }'

    class Meta:
        verbose_name_plural = "Sending of shipments"
        
        
class Reciever(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    custom_id = models.CharField(max_length=8, primary_key=True, default=generate_custom_id, unique=True)
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    status = models.CharField(max_length=20, choices=Status, default="Sending_Shipment")
    percent = models.CharField(max_length=3, default = 0)
    message = models.CharField(max_length=100)
    weight = models.IntegerField()
    length = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()
    
    def __str__(self):
        return f'{ self.user} submitted a request to be sent to {self.name}.This is the ID: {self.custom_id}. Status is : {self.status }'

    class Meta:
        verbose_name_plural = "Recieving a shipments"       

