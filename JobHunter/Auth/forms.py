from django import forms
from django.contrib.auth import get_user_model


class LoginUserForm(forms.Form):
    username = forms.CharField(label="",
                               widget=forms.TextInput(attrs={'class': 'form-input',
                                                             'placeholder': 'Логин'}))
    password = forms.CharField(label="",
                               widget=forms.PasswordInput(attrs={'class': 'form-input',
                                                                 'placeholder': 'Пароль'}))


class RegisterUserForm(forms.ModelForm):
    last_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Фамилия'}))
    first_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Имя'}))
    father_name = forms.CharField(label="", required=False, widget=forms.TextInput(attrs={'placeholder': 'Отчество'}), empty_value=True)
    phone = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Номер телефона',
                                                                    'id': 'phone_number'}))
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Логин'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'Пароль'}))
    password_2 = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder': 'Повтор пароля'}))

    class Meta:
        model = get_user_model()
        fields = ['last_name', 'first_name', 'father_name', 'phone', 'username', 'password', 'password_2']

    def clean_password_2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password_2']:
            raise forms.ValidationError("Пароли не совпадают")
        return cd['password']

    def clean_username(self):
        username = self.cleaned_data['username']
        if get_user_model().objects.filter(username=username).exists():
            raise forms.ValidationError("Пользователь с таким именем уже существует!")
        return username
