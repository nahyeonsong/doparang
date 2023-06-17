from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from pybo.models import Question


def index(request):
    3 / 0  # 강제로 오류발생
    kw = request.GET.get("kw", "")  # 검색어
    question_list = Question.objects.order_by("-create_date")
    if kw:
        question_list = question_list.filter(
            Q(subject__icontains=kw)
            | Q(content__icontains=kw)  # 제목 검색
            | Q(answer__content__icontains=kw)  # 내용 검색
            | Q(author__username__icontains=kw)  # 답변 내용 검색
            | Q(answer__author__username__icontains=kw)  # 질문 글쓴이 검색  # 답변 글쓴이 검색
        ).distinct()
    context = {"question_list": question_list, "kw": kw}
    return render(request, "pybo/question_list.html", context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    context = {"question": question}
    return render(request, "pybo/question_detail.html", context)
