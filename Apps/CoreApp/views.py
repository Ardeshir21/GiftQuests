from django.shortcuts import render
from django.views import generic
from django.core.mail import send_mail


class HomeView(generic.TemplateView):
    template_name = 'CoreApp/Ella/index.html'

    def dispatch(self, request, *args, **kwargs):
        # Any Test Code

        # Call the parent class's dispatch method to continue processing the request
        return super().dispatch(request, *args, **kwargs)