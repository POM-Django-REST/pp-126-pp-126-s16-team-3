from django import forms
from .models import CustomUser


class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            self.add_error('email', 'Email is incorrect')
            return cleaned_data

        if not user.check_password(password):
            self.add_error('password', 'Password is incorrect')
        else:
            self.user = user

        return cleaned_data


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser

        fields = ['email', 'password', 'first_name', 'middle_name', 'last_name', 'role']

    def clean(self):
        cleaned_data = super().clean()
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        first_name = self.cleaned_data.get('first_name')
        middle_name = self.cleaned_data.get('middle_name')
        last_name = self.cleaned_data.get('last_name')

        if email and CustomUser.objects.filter(email=email).exists():
            self.add_error('email', f'Email already exists: {email}')

        if password:
            if len(password) < 6:
                self.add_error('password', 'Password must be at least 6 characters long')
            if password.isdigit():
                self.add_error('password', 'Password must contain at least one letter')

        if first_name and not first_name.isalpha():
            self.add_error('first_name', 'First name must contain only letters')
        if middle_name and not middle_name.isalpha():
            self.add_error('middle_name', 'Middle name must contain only letters')
        if last_name and not last_name.isalpha():
            self.add_error('last_name', 'last_name must contain only letters')

        return cleaned_data

    def save(self, commit=True):
        # In the beginning create a suer object w/o saving to DB
        user = super().save(commit=False)

        # If the role is 1 (librarian)
        if user.role == 1:
            user.is_staff = True
            user.is_superuser = True
        else:
            user.is_staff = False
            user.is_superuser = False

        # Set password via set_password in order to hash the password
        user.set_password(self.cleaned_data.get('password'))

        if commit:
            user.save()
        return user
