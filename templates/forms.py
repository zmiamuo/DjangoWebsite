from django import forms
from django.forms import widgets
from .models import Note, Event

class note(forms.ModelForm):
    title = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder": "Title", "autocomplete": "off", "class": "rounded-lg shadow-sm col-span-6 p-4 bg-blue-200 shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-600 focus:border-transparent","maxlength": "56", "spellcheck": "false"}))
    subject = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder": "Subject", "autocomplete": "off", "class": "rounded-lg shadow-sm col-span-2 p-4 bg-green-200 shadow-sm focus:outline-none focus:ring-2 focus:ring-green-600 focus:border-transparent", "maxlength": "56", "spellcheck": "false"}))
    cue = forms.CharField(label="", widget=forms.Textarea(attrs={"placeholder": "Cue", "autocomplete": "off", "class": "rounded-lg shadow-sm p-4 col-span-2 bg-yellow-200 focus:outline-none shadow-sm focus:ring-2 focus:ring-yellow-600 focus:border-transparent", "maxlength": "1000", "spellcheck": "false"}))
    summary = forms.CharField(label="", widget=forms.Textarea(attrs={"placeholder": "Summary", "autocomplete": "off", "class": "rounded-lg shadow-sm p-4 h-28 mb-5 col-span-8 bg-red-200 shadow-sm focus:outline-none focus:ring-2 focus:ring-red-600 focus:border-transparent", "maxlength": "5000", "spellcheck": "false"}))

    class Meta:
        model = Note

        fields = [
            "subject",
            "title",
            "cue",
            "body",
            "summary"
        ]

themes = [
    ('indigo', 'Getting started'),
    ('green', 'Easy Peasy Lemon Squeezy'),
    ('blue', 'On Track'),
    ('yellow', 'Somewhat Hard'),
    ('red', 'Really Difficult')
]

class event(forms.ModelForm):
    esubject = forms.CharField(label="", widget=forms.TextInput(attrs={"placeholder": "Subject", "autocomplete": "off", "class": "bg-white appearance-none border-2 border-gray-200 rounded-xl w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-indigo-500 h-9","maxlength": "56", "spellcheck": "false"}))
    date = forms.DateField(label="", widget=forms.DateInput(attrs={"placeholder": "Date",'type': 'date', "class": "bg-white appearance-none border-2 border-gray-200 rounded-xl w-full py-2 px-4 text-gray-600 leading-tight focus:outline-none focus:bg-white focus:border-indigo- h-9","maxlength": "56", "spellcheck": "false"}))
    details = forms.CharField(label="", widget=forms.Textarea(attrs={"placeholder": "Details", "autocomplete": "off", "class": "bg-white appearance-none border-2 border-gray-200 rounded-xl w-full py-2 px-4 text-gray-700 leading-tight focus:outline-none focus:bg-white focus:border-indigo-500 h-20","maxlength": "56", "spellcheck": "false"}))
    theme = forms.CharField(label="", widget=forms.Select(choices=themes, attrs={"placeholder": "", "autocomplete": "off", "class": "bg-white appearance-none border-2 border-gray-200 rounded-xl w-full py-2 px-4 text-gray-600 leading-tight focus:outline-none focus:bg-white focus:border-indigo-500 h-10"}))

    class Meta:
        model = Event

        fields = [
            "esubject",
            "date",
            "details",
            "theme"
        ]