from django import forms
from .models import Book, Publisher, Author

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['price', 'rating', 'author', 'publisher']

    price = forms.DecimalField(
        required=True,
        label="Price",
        initial=0
    )

    rating = forms.IntegerField(
        required=True,
        initial=0,
        widget=forms.NumberInput()
    )

    publisher = forms.ModelChoiceField(
        queryset=Publisher.objects.all(),
        required=True,
        label="Publisher",
        widget=forms.Select(attrs={
            'class': "mycssclass",
            'id': 'jsID2'
        })
    )

    author = forms.ModelChoiceField(
        empty_label=None,
        queryset=Author.objects.all(),
        required=True,
        label="Author",
        widget=forms.Select(attrs={
            'class': "mycssclass",
            'id': 'jsID2'
        })
    )
