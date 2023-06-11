from allauth.account.adapter import DefaultAccountAdapter
from django.forms import ValidationError


class RestrictEmailAdapter(DefaultAccountAdapter):
    def clean_email(self, email):
        RestrictedList = ["testuser1@gmail.com", "testuser2@gmail.com"]
        if email in RestrictedList:
            raise ValidationError(
                "You are restricted from registering.\
												Please contact admin."
            )
        return email
