from django.urls import path
from . import views
app_name = 'video'
urlpatterns = [
    # orignal audio removing and voiceover adding page.
    path('', views.audio, name='audio'),
]