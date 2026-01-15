import requests
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import os, json

GROQ_API_KEY = "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"

conversation_history = [
    {"role": "system", "content": "You are a helpful assistant. Always answer in clear bullet points."}
]

@csrf_exempt  
def chat(request):
    if request.method == "POST":
        data = json.loads(request.body)
        message = data.get("message", "")

        conversation_history.append({"role": "user", "content": message})

        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "llama-3.3-70b-versatile",
            "messages": conversation_history,
            "temperature": 0.7
        }

        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            result = response.json()
            reply = result["choices"][0]["message"]["content"]

            conversation_history.append({"role": "assistant", "content": reply})
            return JsonResponse({"reply": reply})
        else:
            return JsonResponse({"error": response.text}, status=response.status_code)
    return render(request, "chatbot.html")

# def bot(request):
#     return render(request, "chatbot.html")
