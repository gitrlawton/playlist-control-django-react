# User-created file.

from django.urls import path
# Importing the template called index (index.html).
from .views import index


# Defining the urlpatterns, just like in the Django-created urls.py file...
urlpatterns = [
    # ...however, instead of writing 'include' after the endpoint (''), we 
    # specify which view we want to be displayed at that endpoint (for example:
    # the 'main' view).
    # Example: path('', main)
    
    # '' means for all endpoints, display the index.html template (our homepage).
    path('', index),
    #
    path('join', index),
    path('create', index),
    # The dynamic path for adding our room code to the url.
    path('room/<str:roomCode>', index),
]