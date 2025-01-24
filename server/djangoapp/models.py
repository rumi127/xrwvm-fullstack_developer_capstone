from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

# Car Make Model
class CarMake(models.Model):
    name = models.CharField(max_length=100)  # Car make name
    description = models.TextField()  # Description of the car make
    # Add any other fields as needed

    def __str__(self):
        return self.name  # Return the name as the string representation


# Car Model Model
class CarModel(models.Model):
    # Define the relationship to CarMake
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE)  # Many-to-One relationship

    name = models.CharField(max_length=100)  # Car model name

    # Define car types as choices
    CAR_TYPES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('COUPE', 'Coupe'),
        ('TRUCK', 'Truck'),
    ]
    type = models.CharField(max_length=10, choices=CAR_TYPES, default='SUV')  # Car type

    dealer_id = models.IntegerField()  # Dealer ID, linked to Cloudant or external database

    year = models.IntegerField(
        default=2023,
        validators=[
            MaxValueValidator(2023),  # Maximum year allowed
            MinValueValidator(2015),  # Minimum year allowed
        ]
    )

    # Add any other fields as needed (e.g., color, mileage)
    color = models.CharField(max_length=30, default='Unknown')  # Example additional field

    def __str__(self):
        return f"{self.name} ({self.car_make})"  # String representation showing name and car make
