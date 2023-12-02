from django import forms
from post_app.models import Post, PostImage

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'context']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'context': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PostImageForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
