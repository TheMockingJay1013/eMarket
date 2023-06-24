from django import forms
from .models import Item 

Input_classes ="w-1/2 py-4 px-6 rounded-xl border"

class NewItemForm(forms.ModelForm) :
    class Meta : 
        model = Item
        fields = ('category' , 'name' , 'description' , 'price' , 'image' ,)
        
        widgets = {
            'category' : forms.Select(attrs={'class':Input_classes}),
            'name' : forms.TextInput(attrs={'class':Input_classes}),
            'description' : forms.Textarea(attrs={'class':Input_classes}),
            'price' : forms.TextInput(attrs={'class':Input_classes}),
            'image' : forms.FileInput(attrs={'class':Input_classes}),
        }
        
class EditItemForm(forms.ModelForm) :
    class Meta : 
        model = Item
        fields = ('name' , 'description' , 'price' , 'image' , 'is_sold')
        
        widgets = {
            'name' : forms.TextInput(attrs={'class':Input_classes}),
            'description' : forms.Textarea(attrs={'class':Input_classes}),
            'price' : forms.TextInput(attrs={'class':Input_classes}),
            'image' : forms.FileInput(attrs={'class':Input_classes}),
        }