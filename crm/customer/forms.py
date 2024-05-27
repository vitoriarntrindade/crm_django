from django import forms

from .models import Customer


class DateInput(forms.DateInput):
    input_type = "date"


class CustomerForm(forms.ModelForm):
    first_name = forms.CharField(
        error_messages={"max_length": "First name cannot be longer than 30 characters"}
    )
    last_name = forms.CharField(
        error_messages={"max_length": "Last name cannot be longer than 30 characterss"}
    )
    email = forms.EmailField()
    birth_date = forms.DateField(widget=DateInput())
    area_code = forms.RegexField(
        regex=r"^\+?1?[0-9]{2}$",
        error_messages={"Invalid": "Invalid area code"}
    )
    phone_number = forms.RegexField(
        regex=r"^\+?1?[0-9]{9,15}$",
        error_messages={"invalid": "Invalid phone number"}
    )
    country = forms.CharField()
    state = forms.CharField()
    city = forms.CharField()

    class Meta:
        model = Customer
        fields = (
            "first_name",
            "last_name",
            "email",
            "birth_date",
            "area_code",
            "phone_number",
            "country",
            "state",
            "city",
        )

