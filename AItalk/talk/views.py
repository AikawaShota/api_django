from django.shortcuts import render
from . import forms
from . import models
import openai


with open('./chatgpt_key.txt') as f:
    chatgpt_api_key = f.readline()
openai.api_key = chatgpt_api_key


def index(request):
    form = forms.ChatForm()
    user_message = "{何も入力されていません}"
    chatgpt_message = "{何も入力されていません}"
    dialogues = models.Dialogue.objects.all()
    if request.method == "POST":
        user_message = "Your message:" + request.POST["message"]
        dialogue = models.Dialogue(
            role="user", context=request.POST["message"])
        dialogue.save()
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": request.POST["message"]}
            ]
        )
        chatgpt_message = "ChatGPT message:" + \
            response["choices"][0]["message"]["content"].lstrip()
        dialogue = models.Dialogue(
            role='chatgpt',
            context=response["choices"][0]["message"]["content"].lstrip())
        dialogue.save()
    context = {
        "form": form,
        "user_message": user_message,
        "chatgpt_message": chatgpt_message,
        "dialogues": dialogues
    }
    return render(request, 'talk/index.html', context)
