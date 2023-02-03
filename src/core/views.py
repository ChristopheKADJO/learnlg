from django.shortcuts import render, redirect
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.
"""
    The IndexView class defines a view for the welcome page. The get method processes GET requests and redirects the authenticated user to the welcome page using redirect('account:welcome'). If the user is not authenticated, the get method simply renders a view for the welcome page using render(request, 'core/index.html').
"""
class IndexView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('account:welcome')
        return render(request, 'core/index.html')

"""
    This function defines the view that will be displayed when a 404 (page not found) error is raised. The function takes as input the HTTP request and an exception, and returns a response using the render method to display the core/404.html template.
""" 
def error_404(request, exception):
    return render(request, 'core/404.html')


"""
    This function defines the view that will be displayed if CSRF protection fails. The function takes as input the HTTP request and an optional reason string that explains the reason for the failure, and returns a response using the render method to display the core/403.html template
""" 
def csrf_failure(request, reason=""):
    return render(request, 'core/403.html')