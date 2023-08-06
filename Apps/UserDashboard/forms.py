#
#
#
#
#
#
# # This is inherited form UserChangeForm from ِDjango app which is ModelForm itself.
# # You must write a views.py for this one.
# class CustomUserUpdateForm(UserChangeForm):
#
#     class Meta(UserChangeForm.Meta):
#         model = UserProfile
#         fields = ['email', 'first_name', 'last_name']
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['email'].disabled = True
#         # Specify any chnage to fields here using widgets
#         self.fields['first_name'].widget.attrs.update({'class': 'special'})
#         self.fields['password'].help_text = "Raw passwords are not stored, so there is no way to see this user's password, but you can change the password from here."
#
#     def save(self, commit=True):
#
#         # Ensure you call the parent class's save.
#         # .save() returns a User object.
#         user = super(CustomUserUpdateForm, self).save()
#
#         # Implement The Changes
#         user.first_name = self.cleaned_data['first_name']
#         user.last_name = self.cleaned_data['last_name']
#         # Make Slug with full name
#         full_name = "{} {}".format(user.first_name, user.last_name)
#         user.slug = slugify(full_name)
#
#         if commit:
#             user.save()
#
#         return user
#
# # This is inherited form UserChangeForm from ِDjango app which is ModelForm itself.
# # You must write a views.py for this one.
# class CustomUserPasswordChangeForm(PasswordChangeForm):
#     def Meta():
#         model = UserProfile