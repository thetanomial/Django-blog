from django import forms 

from blog.models import BlogPost

class BlogCreateForm(forms.ModelForm):

    class Meta:
        model = BlogPost
        fields = ['title','description']