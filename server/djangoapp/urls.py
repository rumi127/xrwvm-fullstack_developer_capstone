from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views  # Import views

app_name = 'djangoapp'

urlpatterns = [
    # Path for registration (to be added later)

    # Path for login
    path(route='login', view=views.login_user, name='login'),
    # Path for logout
    path('logout/', views.logout_request, name='logout'),
    # Path for Get cars
    path('get_cars', views.get_cars, name='getcars'),

    # Path for Get dealerships
    path(route='get_dealers', view=views.get_dealerships, name='get_dealers'),
    path(route='get_dealers/<str:state>', view=views.get_dealerships, name='get_dealers_by_state'),

    # Path for Get dealer details
    path(route='dealer/<int:dealer_id>', view=views.get_dealer_details, name='dealer_details'),

    # Path for Get dealer reviews
    path(route='reviews/dealer/<int:dealer_id>', view=views.get_dealer_reviews, name='dealer_reviews'),

    # Path for adding a review view (to be added later)
    path(route='add_review', view=views.add_review, name='add_review'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
