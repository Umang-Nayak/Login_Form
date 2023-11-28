from django import forms
from Fast.models import UserDetails


class UserForm(forms.ModelForm):
    class Meta:
        model = UserDetails
        fields = ["u_fname", "u_lname", "u_contact", "u_address", "u_email", "u_password"]
