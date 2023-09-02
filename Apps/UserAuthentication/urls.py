# This file is mostly copied from allAuth in order to have some modification on views and url patterns
from django.urls import path, re_path
from . import views
from importlib import import_module
from django.urls import include, path
from allauth.socialaccount import providers
from allauth import app_settings


# app_name = 'UserAthentication'


urlpatterns = [
        path('login/', views.CustomLoginView.as_view(), name='account_login'),
        path('register/', views.CustomRegisterView.as_view(), name='account_signup'),
        path("logout/", views.CustomLogoutView.as_view(), name="account_logout"),

        # E-mail
        # path("email/", views.CustomEmailView.as_view(), name="account_email"),
        path(
                "confirm-email/",
                views.CustomEmailVerificationSentView.as_view(),
                name="account_email_verification_sent",
        ),
        re_path(
                r"^confirm-email/(?P<key>[-:\w]+)/$",
                views.CustomConfirmEmailView.as_view(),
                name="account_confirm_email",
        ),

        # password reset
        path("password/reset/", views.CustomPasswordResetView.as_view(), name="account_reset_password"),
        path(
                "password/reset/done/",
                views.CustomPasswordResetDoneView.as_view(),
                name="account_reset_password_done",
        ),
        re_path(
                r"^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
                views.CustomPasswordResetFromKeyView.as_view(),
                name="account_reset_password_from_key",
        ),
        path(
                "password/reset/key/done/",
                views.CustomPasswordResetFromKeyDoneView.as_view(),
                name="account_reset_password_from_key_done",
        ),

]



# Social Accounts
if app_settings.SOCIALACCOUNT_ENABLED:
    urlpatterns += [path("social/", include("allauth.socialaccount.urls"))]

# Provider urlpatterns, as separate attribute (for reusability).
provider_urlpatterns = []
for provider in providers.registry.get_list():
    try:
        prov_mod = import_module(provider.get_package() + ".urls")
    except ImportError:
        continue
    prov_urlpatterns = getattr(prov_mod, "urlpatterns", None)
    if prov_urlpatterns:
        provider_urlpatterns += prov_urlpatterns
urlpatterns += provider_urlpatterns