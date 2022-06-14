
'''
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView

from ..forms import CustomerSignUpForm
from ..models import User ,ProfileCustomer

class CustomerSignUpView(CreateView):
    model = User
    form_class = CustomerSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'customer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return True
'''