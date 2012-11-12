from django.shortcuts import get_object_or_404, redirect, render
from django.template.defaultfilters import slugify
from django.views.generic import View

from django.contrib.auth.decorators import login_required

from . import forms
from .models import Comment, Post


def index(request):
    return render(request, "content/index.html", {
        "posts": Post.objects.all(),
        "comments": Comment.objects.all(),
    })


class EditPostView(View):

    def _get_object(self, request, post_id):
        if post_id is None:
            return Post(poster=request.user)
        else:
            return get_object_or_404(Post, id=post_id, poster=request.user)

    def _render(self, request, form):
        return render(request, "content/post_edit.html", {
            "post": form.instance,
            "form": form,
        })

    def get(self, request, post_id=None, slug=None):
        post = self._get_object(request, post_id)
        form = forms.PostForm(instance=post)
        return self._render(request, form)

    def post(self, request, post_id=None, slug=None):
        post = self._get_object(request, post_id)
        form = forms.PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect("post_view", post.id, slugify(post.title))
        return self._render(request, form)

post_edit = login_required(EditPostView.as_view())


def post_view(request, post_id, slug=None):
    post = get_object_or_404(Post, id=post_id)
    return render(request, "content/post_view.html", {
        "post": post,
    })
