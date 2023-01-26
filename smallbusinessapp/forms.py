from django.contrib.auth.forms import AuthenticationForm, UsernameField, UserCreationForm

from django import forms

from users.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'