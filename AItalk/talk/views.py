from django.shortcuts import render
from . import forms
import openai


with open('./chatgpt_key.txt') as f:
    chatgpt_api_key = f.readline()
openai.api_key=chatgpt_api_key

# Create your views here.
def index(request):
    form = forms.ChatForm()
    user_message = "{何も入力されていません}"
    chatgpt_message = "{何も入力されていません}"
    if request.method == "POST":
        user_message = "Your message:" + request.POST["message"]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": request.POST["message"]}
            ]
        )
        chatgpt_message = "ChatGPT message:" + response["choices"][0]["message"]["content"].lstrip()
    context = {
        "form": form,
        "user_message": user_message,
        "chatgpt_message": chatgpt_message
    }
    return render(request, 'talk/index.html', context)
