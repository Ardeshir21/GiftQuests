from django.urls import reverse_lazy



AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    'django.contrib.auth.backends.ModelBackend',

    # `allauth` specific authentication methods, such as login by e-mail
    'allauth.account.auth_backends.AuthenticationBackend',
]


AUTH_USER_MODEL = 'UserAuthentication.UserProfile'

ACCOUNT_EMAIL_VERIFICATION = 'none'

ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
LOGIN_REDIRECT_URL = reverse_lazy('CoreApp:index')
LOGIN_URL = reverse_lazy('account_login')
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE  = False
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
ACCOUNT_MAX_EMAIL_ADDRESSES = 1
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True


ACCOUNT_FORMS = {
    # 'signup': 'apps.accountApp.forms.CustomSignupForm',
    # 'login': 'apps.accountApp.forms.CustomLoginForm',
    # 'reset_password': 'Apps.UserAuthentication.forms.CustomResetPasswordForm'
}

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}