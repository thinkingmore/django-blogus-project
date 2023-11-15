from django import forms
from .models import Post

class AddPostForm(forms.ModelForm):  
    class Meta:
        model = Post
        fields = ['title', 'slug', 'image', 'categories', 'content', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Title'})
        self.fields['content'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Add blog content'})
        self.fields['image'].widget.attrs.update({'class': 'form-control','style': 'width: 250px;'})
        self.fields['slug'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Add slug'})
        self.fields['categories'].widget.attrs.update({'class': 'form-select','style': 'width: 150px;', 'placeholder': 'Add slug'})
        self.fields['status'].widget.attrs.update({'class': 'form-select','style': 'width: 120px;', 'placeholder': 'Add slug'})