from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import Post
from django_quill.fields import QuillField

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields =['username','email','password1','password2']
        help_texts = {k:"" for k in fields }

class PostForm(forms.ModelForm):
    content = QuillField(forms.CharField(label='', widget=forms.Textarea(attrs={'rows':2, 'placerholder':'¿que estas pensando?'}), required=True))


    class Meta:
        model = Post
        fields =['titulo','subtitulo','content','imagen']