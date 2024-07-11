# User-created file.
# Stores all the urls pertaining to this app.
# We have set this project up to funnel all urls to the urls.py file in
# the project folder (playlist_controller), and then forward them to this file.

from django.urls import path
# Importing the view called RoomView from the views.py file.
from .views import RoomView

# Defining the urlpatterns, just like in the Django-created urls.py file...
urlpatterns = [
    # ...however, instead of writing 'include' after the endpoint (''), we 
    # specify which view we want to be displayed at that endpoint (for example:
    # the 'main' view).
    # Example: path('', main)
    
    # To use our view, we want to add .as_view() after the name.
    # This path displays our RoomView when the /room endpoint is visited.
    path('room', RoomView.as_view()),
]