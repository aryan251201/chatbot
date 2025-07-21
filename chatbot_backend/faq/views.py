from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status
from .models import FAQ
from .serializers import FAQSerializers
import os
import openai
from django.conf import settings
from rest_framework.views import APIView




class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all().order_by('-created_at')
    serializer_class = FAQSerializers


class AskView(APIView):
    def post(self, request):
        question = request.data.get("question")
        if not question:
            return Response({"error": "Question is required."}, status=status.HTTP_400_BAD_REQUEST)

        openai.api_key = settings.OPENAI_API_KEY

        context_faqs = FAQ.objects.all()
        context_text = "\n".join([f"Q: {faq.question}\nA: {faq.answer}" for faq in context_faqs])

        prompt = f"""
You are a helpful assistant for a marketing company. Use the FAQ below to answer user questions. If the answer is not available, say "Sorry, I don't know that yet."

FAQs:
{context_text}

User Question: {question}
Answer:"""

        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.3,
                max_tokens=300
            )
            answer = response.choices[0].message.content.strip()
            return Response({"answer": answer})

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


print(os.getenv("OPENAI_API_KEY"))
