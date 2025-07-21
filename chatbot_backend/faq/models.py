from django.db import models


class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()
    embedding = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add= True)

    
    def __str__(self):
        return self.question[:50]


class ChatQuery(models.Model):
    user_question = models.TextField()
    ai_answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
