from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="author_question"
    )
    authoropp = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="authoropp_questionopp"
    )
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name="voter_question")  # 추천인 추가
    voteropp = models.ManyToManyField(
        User, related_name="voteropp_questionopp"
    )  # 반대인 추가

    def __str__(self):
        return self.subject


class Answer(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="author_answer"
    )
    authoropp = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="authoropp_answeropp"
    )
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name="voter_answer")
    voteropp = models.ManyToManyField(User, related_name="voteropp_answeropp")

    def __str__(self):
        return self.content


# Create your models here.
