from django.shortcuts import render
def audio(request):
    """The page for generating spoken tutorials."""
    return render(request,
        'D:/Coding/Automated-Spoken-Tutorials/project/templates/video/video.html')