from django import forms

class LocationForm(forms.Form):
    from_location = forms.CharField(label="From Location", max_length=100)
    to_location = forms.CharField(label="To Location", max_length=100)
    travel_date = forms.DateField(label="Travel Date")
