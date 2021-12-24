from django import forms
from .models import myText

class LectureForm(forms.ModelForm):
    class Meta:
        model=myText
        fields= (
            'title',
            'contents',
            'img_url',
            'category',
            'board_text',
            'lecture_title1',
            'lecture_vidio1',
            'lecture_title2',
            'lecture_vidio2',
            'lecture_title3',
            'lecture_vidio3',
            'lecture_title4',
            'lecture_vidio4',
        )