from django.contrib import admin
from django.urls import path

# index는 대문, blog는 게시판
from main.views import index, blog, posting

from .views import (
    base_views,
    question_views,
    answer_views,
)

# 이미지를 업로드하자
from django.conf.urls.static import static
from django.conf import settings

app_name = "pybo"


urlpatterns = [
    # base_views.py
    path("", base_views.index, name="index"),
    path("<int:question_id>/", base_views.detail, name="detail"),
    # question_views.py
    path("question/create/", question_views.question_create, name="question_create"),
    path(
        "question/modify/<int:question_id>/",
        question_views.question_modify,
        name="question_modify",
    ),
    path(
        "question/delete/<int:question_id>/",
        question_views.question_delete,
        name="question_delete",
    ),
    # answer_views.py
    path(
        "answer/create/<int:question_id>/",
        answer_views.answer_create,
        name="answer_create",
    ),
    path(
        "answer/modify/<int:answer_id>/",
        answer_views.answer_modify,
        name="answer_modify",
    ),
    path(
        "answer/delete/<int:answer_id>/",
        answer_views.answer_delete,
        name="answer_delete",
    ),
    path(
        "question/vote/<int:question_id>/",
        question_views.question_vote,
        name="question_vote",
    ),
    path(
        "answer/vote/<int:answer_id>/",
        answer_views.answer_vote,
        name="answer_vote",
    ),
    path("admin/", admin.site.urls),
    # 웹사이트의 첫화면은 index 페이지이다 + URL이름은 index이다
    path("", index, name="index"),
    # URL:80/blog에 접속하면 blog 페이지 + URL이름은 blog이다
    path("blog/", blog, name="blog"),
    # URL:80/blog/숫자로 접속하면 게시글-세부페이지(posting)
    path("blog/<int:pk>/", posting, name="posting"),
]

# 이미지 URL 설정
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
