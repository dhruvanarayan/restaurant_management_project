from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Note

@login_required
def my_notes(request):
    # Only show logged-in user's notes
    notes = Note.objects.filter(user=request.user)
    return render(request, 'account/my_notes.html', {'notes': notes})

@login_required
def add_note(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Note.objects.create(user=request.user, title=title, content=content)
        return redirect('my_notes')
    return render(request, 'account/add_note.html')
