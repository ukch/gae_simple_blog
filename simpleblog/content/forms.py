import datetime

from django import forms
from django.core import validators

from .models import Post, Comment


class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "input-block-level"
        self.fields["datetime_posted"].required = False

    def clean_datetime_posted(self):
        data = self.cleaned_data["datetime_posted"]
        if data in validators.EMPTY_VALUES:
            return datetime.datetime.now()
        return data

    class Meta:
        model = Post
        fields = ("title", "body", "datetime_posted")


class CommentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields["body"].widget.attrs["class"] = "input-xxlarge"

    class Meta:
        model = Comment
        fields = ("body", )
