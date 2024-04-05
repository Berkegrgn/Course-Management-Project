from django import forms
from django.forms import SelectMultiple, TextInput, Textarea
from ckeditor.fields import RichTextField
from courses.models import Course
from .models import Comment


# class CourseCreateForm(forms.Form):
#     title = forms.CharField(
#         label="kurs başlığı",
#         required=True, 
#         error_messages= {
#             "required":"kurs başlığı girmelisiniz."}, 
#         widget=forms.TextInput(attrs={"class":"form-control"}))
        
#     description = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))
#     imageUrl = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     slug = forms.SlugField(widget=forms.TextInput(attrs={"class":"form-control"}))

class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title','description','image','slug')
        labels = {
            'title':"Kurs başlığı",
            'description':'Açıklama'
        }
        widgets = {
            "title": TextInput(attrs={"class":"form-control"}),
            "description": Textarea(attrs={"class":"form-control"}),
            "slug": TextInput(attrs={"class":"form-control"}),
        }
        error_messages = {
            "title": {
                "required":"Kurs başlığı girmelisiniz.",
                "max_length": "Maksimum 50 karakter girmelisiniz"
            },
            "description": {
                "required":"Kurs açıklaması gereklidir."
            }
        }
        
class CourseEditForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title','description','image','slug','categories','isActive')
        labels = {
            'title':"Kurs Başlığı",
            'description':'Açıklama'
        }
        widgets = {
            "title": TextInput(attrs={"class":"form-control"}),
            "description": Textarea(attrs={"class":"form-control"}),
            "slug": TextInput(attrs={"class":"form-control"}),
            "categories": SelectMultiple(attrs={"class":"form-control"})

        }
        error_messages = {
            "title": {
                "required":"kurs başlığı girmelisiniz.",
                "max_length": "maksimum 50 karakter girmelisiniz"
            },
            "description": {
                "required":"kurs açıklaması gereklidir."
            }
        }

        
class UploadForm(forms.Form):
    image = forms.ImageField()


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text','rating')
        widgets = {
            'text':Textarea(attrs={'class':'form-control','row':4,'col':50}),
            'rating': forms.Select(choices=[(i, f"{i:.1f}") for i in range(1, 6)])
        }
        labels = {
            'text':"",
            'rating':''
        }

class DeleteCommentForm(forms.Form):
    comment_id = forms.IntegerField(widget=forms.HiddenInput)
