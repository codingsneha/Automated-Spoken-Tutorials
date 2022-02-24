from django.shortcuts import render
def voiceover(request):
    """The page for generating voiceover."""
    return render(request,
        'D:/Coding/Automated-Spoken-Tutorials/project/templates/tts/voiceover.html')