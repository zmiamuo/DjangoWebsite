from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import User, Note, Event
from .forms import note, event

import requests

def index(request):
    return render(request, "snotes/index.html")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("notes", args=[user.id]))
        else:
            return render(request, "snotes/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "snotes/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "snotes/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "snotes/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("notes", args=[user.id]))
    else:
        return render(request, "snotes/register.html")

@login_required
def notes(request, userid):
    notes = Note.objects.all().filter(author=userid)
    return render(request, "snotes/notes.html", {"notes": notes})

# Using Youtube API for creating a new note
def create(request):
    videos = []

    if request.method == 'POST':
        # Request from the YOUTUBE API
        search_url = 'https://www.googleapis.com/youtube/v3/search'
        video_url = 'https://www.googleapis.com/youtube/v3/videos'

        video_ids = []

        search_params = {
            'key': settings.YOUTUBE_API,
            'part': 'snippet',
            'q': request.POST['search'],
            'maxResults': 8,
            'type': 'video'
        }

        r1 = requests.get(search_url, params=search_params)
        results = r1.json()['items']

        for result in results:
            video_ids.append(result['id']['videoId'])

        video_params = {
            'key': settings.YOUTUBE_API,
            'id': ','.join(video_ids),
            'part': 'snippet',
            'maxResults': 8
        }

        r2 = requests.get(video_url, params=video_params)

        results = r2.json()['items']

        for result in results:
            video_data = {
                'id': result['id'],
                'thumbnail': result['snippet']['thumbnails']['high']['url'],
                'title': result['snippet']['title'],
                'channel': result['snippet']['channelTitle']
            }
            videos.append(video_data)

    return render(request, "snotes/create.html", {"videos": videos})

def newnote(request, videoid):
    if request.method == "POST":
        user = request.user
        newNote = note(request.POST)

        if newNote.is_valid():
            noteBody = newNote.cleaned_data['body']
            noteTitle = newNote.cleaned_data['title']
            noteSubject = newNote.cleaned_data['subject']
            noteSummary = newNote.cleaned_data['summary']
            noteCues = newNote.cleaned_data['cue']

            nNote = Note(author=request.user, title=noteTitle, body=noteBody, summary=noteSummary, cue=noteCues, subject=noteSubject)
            nNote.save()

            return redirect(reverse('notes', args=[user.id]))
        else:
            return render(request, "snotes/newnote.html", {"form": note, "video_id": videoid})

    elif request.method == "GET":
        return render(request, "snotes/newnote.html", {"form": note, "video_id": videoid})

def note_view(request, id):
    note = Note.objects.get(id=id)
    return render(request, "snotes/note.html", {"note": note})

def subject_view(request, subj):
    if request.method == "GET":
        notes = Note.objects.all().filter(author=request.user, subject=subj)

        return render(request, "snotes/subject.html", {"notes": notes, "subject": subj})

def edit_note(request, title):
    noteUpdate = Note.objects.get(title=title)
    form = note(instance=noteUpdate)

    if request.method == "POST":
        # Pre-populate form with existing content
        form = note(request.POST, instance=noteUpdate)

        if form.is_valid():
            form.save()

            return redirect(reverse('note', args=[noteUpdate.id]))

    return render(request, "snotes/editnote.html", {'form': form, "title": title})

def delete_note(request, title):
    user = request.user
    Note.objects.filter(title=title).delete()

    return redirect(reverse('notes', args=[user.id]))

@csrf_exempt
def calendar_view(request):
    if request.method == "GET":
        events = Event.objects.all().filter(author=request.user)
        return render(request, "snotes/calendar.html", {'form': event, 'events': events})

    elif request.method == "POST":

        newEvent = event(request.POST)

        if newEvent.is_valid():
            eventSubject = newEvent.cleaned_data['esubject']
            eventDate = newEvent.cleaned_data['date']
            eventDetails = newEvent.cleaned_data['details']
            eventTheme = newEvent.cleaned_data['theme']

            newEvent = Event(author=request.user, esubject=eventSubject, date=eventDate, details=eventDetails, theme=eventTheme)
            newEvent.save()

            return redirect(reverse('calendar'))
        else:
            return render(request, "snotes/calendar.html")


def delete_event(request, subject):
    Event.objects.filter(esubject=subject).delete()

    return redirect(reverse('calendar'))
