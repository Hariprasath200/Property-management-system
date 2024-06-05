from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)
    near_hotel = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class Bus(models.Model):
    name = models.CharField(max_length=100)
    from_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='departure_buses')
    to_location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='arrival_buses')
    travel_date = models.DateField()

    def __str__(self):
        return f'{self.name} - {self.from_location} to {self.to_location}'

class Hotel(models.Model):
    name = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='hotels')

    def __str__(self):
        return self.name

class DepositCenter(models.Model):
    name = models.CharField(max_length=100)
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='deposit_centers')

    def __str__(self):
        return self.name
