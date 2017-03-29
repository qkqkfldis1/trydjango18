from django import forms

from .models import Lecture


class LectureForm(forms.ModelForm):
    class Meta:
        model = Lecture
        fields = [
            "title",
            "content",
            "publish",
            "keyword1",
            "keyword2",
            "keyword3",
            "keyword4",
            "keyword5",
        ]