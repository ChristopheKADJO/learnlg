from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.urls import reverse_lazy
from accounts.models import CustomUser
from django.views.generic import CreateView, DeleteView, View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from accounts.forms import LoginForm, UserRegistrationForm

"""
AuthenticatedUserMixin is a Django class that provides a dispatch function which checks if the currently logged-in user is authenticated. If the user is authenticated, they will have access to the 'account:welcome' view. If not, the function will not redirect the user and they will not have access to the view.
"""
# https://docs.djangoproject.com/fr/4.0/ref/class-based-views/base/#django.views.generic.base.View.dispatch
class AuthenticatedUserMixin:
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('account:welcome')
        return super().dispatch(request, *args, **kwargs)


"""
RegisterView is a class-based view that handles user registration. It uses the UserRegistrationForm form to gather user data and creates a new user object upon successful form submission. The AuthenticatedUserMixin is used to check if the user is already authenticated, in which case the user will be redirected to the welcome page. If the user is not authenticated, the CreateView will handle the creation of a new user object.
"""
class RegisterView(AuthenticatedUserMixin, CreateView):
    form_class = UserRegistrationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('account:welcome')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response
    
    
"""
The MyLoginView class is a custom LoginView class that inherits from AuthenticatedUserMixin and LoginView classes. It defines the template name to use for the login page as 'accounts/login.html' and sets the form class to LoginForm.
"""
class MyLoginView(AuthenticatedUserMixin, LoginView):
    template_name = 'accounts/login.html'
    form_class = LoginForm
    

"""
The DeleteUserView is a login-protected view for deleting a user's account using a CustomUser model. It specifies the confirmation template and a success URL, and limits the deletion to only the current user's account.
"""
@method_decorator(login_required, name='dispatch')
class DeleteUserView(DeleteView):
    model = CustomUser
    template_name = 'accounts/confirm_delete.html'
    success_url = reverse_lazy('core:index')
    
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(id=self.request.user.id)


"""
The WelcomeView class defines a view for a welcome page accessible only to the authenticated user.
The get method displays the user's first name using an HTML template.
"""
@method_decorator(login_required, name='dispatch')
class WelcomeView(View):
    def get(self, request):
        firstname = self.request.user.firstname
        return render(request, 'accounts/welcomepage.html', {'firstname': firstname})

