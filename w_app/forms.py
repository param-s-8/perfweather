from django.forms import ModelForm, TextInput
from .models import City,DeetCity,Feedback

class CityForm(ModelForm):
    class Meta:
        model = City
        fields=['name']
        widgets={'name':TextInput(attrs={'class':'input','placeholder':'City Name'})}
        
class DeetCityForm(ModelForm):
    class Meta:
        model = DeetCity
        fields=['name']
        widgets={'name':TextInput(attrs={'class':'input','placeholder':'City Name'})}

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        exclude=[]