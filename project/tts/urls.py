from django.urls import path
from . import views
app_name = 'tts'
urlpatterns = [
    # voiceover generation page.
    path('', views.voiceover, name='voiceover'),
]