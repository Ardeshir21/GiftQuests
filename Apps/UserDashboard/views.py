# from django.shortcuts import render
# from django.contrib.auth.views import PasswordChangeView
# from django.views import generic
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.contrib import messages
# from django.urls import reverse_lazy, reverse
# from .models import UserProfile
# from . import forms
#
#
# # Here is the Extra Context dictionary which is used in get_context_data of Views classes
# def get_extra_context():
#     extraContext = {
#
#         }
#     return extraContext
#
#
# # the Django-allAuth application is used for User views
# # The Update view is not in the AllAuth app
#
# # User Update
# class UserUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
#     form_class = forms.CustomUserUpdateForm
#     model = UserProfile
#     template_name = 'UserAthentication/update_user.html'
#
#
#     # If the user change the url manually, this get method will handle the issues
#     def get(self, request, *args, **kwargs):
#         # Check if the id and slug of logged in user is in concert with the URL request
#         if self.request.user.pk != self.kwargs['user_id'] or self.request.user.slug != self.kwargs['full_name']:
#             return HttpResponseRedirect(reverse("UserAthentication:user-update", kwargs={'user_id':self.request.user.pk,
#                                                                                                 'full_name':self.request.user.slug}))
#         else:
#             return super().get(self.request, *args, **kwargs)
#
#     # To query the exact row that we are looking in PersonalProfile table
#     def get_object(self):
#         return self.model.objects.get(id=self.request.user.pk)
#
#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super().get_context_data(**kwargs)
#         # Append shared extraContext
#         context.update(get_extra_context())
#         # Current User
#         context['TheUser'] = self.get_object()
#         # Defaul value for is_private
#         context['is_private'] = False
#         # if the current user is in her own page
#         if self.request.user.pk == self.kwargs['user_id'] and self.request.user.slug == self.kwargs['full_name']:
#             context['is_private'] = True
#         return context
#
# # User Password Change
# class UserPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
#     form_class = forms.CustomUserPasswordChangeForm
#     model = UserProfile
#     template_name = 'UserAthentication/password_change.html'
#
#     def get_success_url(self):
#         return reverse("resumeApp:personal-resume-private", kwargs={'user_id':self.request.user.pk,
#                                                                 'full_name':self.request.user.slug})
#
#     # If the user change the url manually, this get method will handle the issues
#     def get(self, request, *args, **kwargs):
#         # Check if the id and slug of logged in user is in concert with the URL request
#         if self.request.user.pk != self.kwargs['user_id'] or self.request.user.slug != self.kwargs['full_name']:
#             return HttpResponseRedirect(reverse("UserAthentication:password-change", kwargs={'user_id':self.request.user.pk,
#                                                                                     'full_name':self.request.user.slug}))
#         else:
#             return super().get(self.request, *args, **kwargs)
#
#     # To query the exact row that we are looking in PersonalProfile table
#     def get_object(self):
#         return self.model.objects.get(id=self.request.user.pk)
#
#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super().get_context_data(**kwargs)
#         # Append shared extraContext
#         context.update(get_extra_context())
#         # Current User
#         context['TheUser'] = self.get_object()
#         # Defaul value for is_private
#         context['is_private'] = False
#         # if the current user is in her own page
#         if self.request.user.pk == self.kwargs['user_id'] and self.request.user.slug == self.kwargs['full_name']:
#             context['is_private'] = True
#         return context
