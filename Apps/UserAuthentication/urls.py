from django.urls import path, re_path
# from allauth.account import views as allAuthViews
from . import views

# app_name = 'UserAthentication'


urlpatterns = [
        # path('login/', views.CustomLoginView.as_view(), name='account_login'),
        # path('register/', views.CustomRegisterView.as_view(), name='account_signup'),
        # path("logout/", views.CustomLogoutView.as_view(), name="account_logout"),
        #
        # # E-mail
        # # path("email/", views.CustomEmailView.as_view(), name="account_email"),
        # path(
        #         "confirm-email/",
        #         views.CustomEmailVerificationSentView.as_view(),
        #         name="account_email_verification_sent",
        # ),
        # re_path(
        #         r"^confirm-email/(?P<key>[-:\w]+)/$",
        #         views.CustomConfirmEmailView.as_view(),
        #         name="account_confirm_email",
        # ),
        #
        # # password reset
        # path("password/reset/", views.CustomPasswordResetView.as_view(), name="account_reset_password"),
        # path(
        #         "password/reset/done/",
        #         views.CustomPasswordResetDoneView.as_view(),
        #         name="account_reset_password_done",
        # ),
        # re_path(
        #         r"^password/reset/key/(?P<uidb36>[0-9A-Za-z]+)-(?P<key>.+)/$",
        #         views.CustomPasswordResetFromKeyView.as_view(),
        #         name="account_reset_password_from_key",
        # ),
        # path(
        #         "password/reset/key/done/",
        #         views.CustomPasswordResetFromKeyDoneView.as_view(),
        #         name="account_reset_password_from_key_done",
        # ),

]
