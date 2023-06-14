from django.shortcuts import render

from allauth.account.views import EmailVerificationSentView


class CustomEmailVerificationSentView(EmailVerificationSentView):
    template_name = "account/confirm_email.html"
