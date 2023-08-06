from django.shortcuts import render
from django.views import generic
from allauth.account.views import LoginView, SignupView, \
                                    ConfirmEmailView, EmailView, \
                                    EmailVerificationSentView, LogoutView, \
                                    PasswordResetView, PasswordResetDoneView, \
                                    PasswordResetFromKeyView, PasswordResetFromKeyDoneView

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


# The views are inherited from allAuth to override them if needed.
# In addition, the urls.py is also customized

# Login View
class CustomLoginView(LoginView):
    '''
    This view is inherited from allAuth LoginView to ovveride the template and messages
    '''

    def form_invalid(self, form):
        # Add an error message for invalid form data
        messages.error(self.request, 'Invalid email or password. Please correct the errors and try again.')
        return super().form_invalid(form)


# Signup View
class CustomRegisterView(SignupView):

    def form_valid(self, form):
        # Add messages
        errors_dict = form.errors.as_data() # use this one to create different messages from the form
        if True: # Use this one to check if the user exists
            messages.error(self.request, 'This email has been already registered.')

        return super().form_valid(form)


# Email View
# This view is to add or change the emails. It's disabled using ACCOUNT_MAX_EMAIL_ADDRESSES
# class CustomEmailView(LoginRequiredMixin, EmailView):
#     pass

# Email Verification View
class CustomEmailVerificationSentView(EmailVerificationSentView):
    pass

# Confirm Email View
class CustomConfirmEmailView(ConfirmEmailView):
    pass

# Logout View
class CustomLogoutView(LogoutView):
    pass

# Password Reset View
class CustomPasswordResetView(PasswordResetView):
    pass

# Password Reset Done View
class CustomPasswordResetDoneView(PasswordResetDoneView):
    pass

# Password Reset From Key View
class CustomPasswordResetFromKeyView(PasswordResetFromKeyView):
    pass

# Password Reset From Key Done View
class CustomPasswordResetFromKeyDoneView(PasswordResetFromKeyDoneView):
    pass



