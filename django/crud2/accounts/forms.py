from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
#from .models import User 직접참조는 권장하지 않음
from django.contrib.auth import get_user_model

'''
class AccountForm(forms.Form):
    title = forms.CharField(max_length=10)
    content = forms.CharField()
'''


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        #model = User
        model = get_user_model()

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('email','first_name','last_name',)