from django.shortcuts import render, redirect
from .forms import PostForm


def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect(
                "question_list"
            )  # Replace 'post_list' with the name of your post list view
    else:
        form = PostForm()

    return render(request, "create_post.html", {"form": form})
