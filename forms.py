from django import forms
from django.forms import ModelForm, ValidationError
from demo_app.models import BankAccount, AppUser , Article
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm



# class BankAccountform(forms.Form):
#     name_in_bank = forms.CharField()
#     account_no= forms.IntegerField()
#     ifsc_code = forms.CharField()
#     location = forms.CharField()

    # class meta:
    #     fields = "__all__"

class BankAccountModelsForm(ModelForm):
    class Meta:
        model = BankAccount
        fields = "__all__"        


class SignUpForm(UserCreationForm):
    class Meta:
        model = AppUser
        fields = ("username", "email", "password1", "password2",)

class LoginForm(AuthenticationForm):
    pass

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ("title", "body", "tag")




