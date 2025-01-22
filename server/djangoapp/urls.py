# Uncomment the imports before you add the code
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views  # Import views from the current app

app_name = 'djangoapp'

urlpatterns = [
    # Path for registration (to be added later)

    # Path for login
    path(route='login', view=views.login_user, name='login'),
    # Path for logout
    path('logout/', views.logout_request, name='logout'),

    # Path for dealer reviews view (to be added later)

    # Path for adding a review view (to be added later)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
