from django import forms

from .models import item , Catagory , author , publisher , orders

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    class Meta:
        model = item
        fields = ['catagory','name', 'description', 'price', 'image' , 'author'  , 'publisher']
        name = forms.TextInput()
        description =  forms.Textarea ()
        price =  forms.TextInput()
        image  =  forms.FileInput()
        catagoey =forms.ModelMultipleChoiceField(
        queryset=Catagory.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
        publsiher =forms.ModelMultipleChoiceField(
        queryset=Catagory.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
        author =forms.ModelMultipleChoiceField(
        queryset=Catagory.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

class EditItemForm(forms.ModelForm):
    class Meta:
        model = item
        fields = ('name', 'description', 'price', 'image', 'is_sold' , 'author' , 'publisher' , 'catagory')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
            'price': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),

        }
        catagoey =forms.ModelMultipleChoiceField(
        queryset=Catagory.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
        publsiher =forms.ModelMultipleChoiceField(
        queryset=Catagory.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
        author =forms.ModelMultipleChoiceField(
        queryset=Catagory.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )
class OrderForm(forms.ModelForm):
    class Meta:
        model = orders
        fields = ('create_bt' ,)
        create_bt = forms.TextInput()
