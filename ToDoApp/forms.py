from django import forms


class ToDoForm(forms.Form):
    text = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add your Todo...'}))
