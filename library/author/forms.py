from django import forms
from .models import Author


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author

        # Fields that are shown in the form
        fields = ['name', 'surname', 'patronymic']

    def clean(self):
        cleaned_data = super().clean()
        name = self.cleaned_data.get('name')
        surname = self.cleaned_data.get('surname')
        patronymic = self.cleaned_data.get('patronymic')

        if name and not name.isalpha():
            self.add_error('name', 'Name must contain only letters')
        if surname and not surname.isalpha():
            self.add_error('surname', 'Surname must contain only letters')
        if patronymic and not patronymic.isalpha():
            self.add_error('patronymic', 'Patronymic must contain only letters')

        return cleaned_data
