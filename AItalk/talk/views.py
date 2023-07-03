from django.shortcuts import render, redirect
from . import forms
from . import models
import openai


with open('./chatgpt_key.txt') as f:
    chatgpt_api_key = f.readline()
openai.api_key = chatgpt_api_key


def index(request):
    form = forms.ChatForm()
    dialogues = models.Dialogue.objects.all()
    if request.method == "POST":
        form = forms.ChatForm(request.POST)
        if form.is_valid():
            dialogue = models.Dialogue(
                role="user", context=request.POST["message"])
            dialogue.save()
            history = []
            for i in dialogues:
                history.append({"role": i.role, "content": i.context})
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=history
            )
            dialogue = models.Dialogue(
                role='assistant',
                context=response["choices"][0]["message"]["content"].lstrip())
            dialogue.save()
            return redirect("talk:index")
    context = {
        "form": form,
        "dialogues": dialogues
    }
    return render(request, 'talk/index.html', context)


def delete(request):
    if request.method == "POST":
        models.Dialogue.objects.all().delete()
    return redirect("talk:index")


def american(request):
    if request.method == "POST":
        models.Dialogue.objects.all.delete()
        dialogue = models.Dialogue(
            role="system",
            context="今後の返信は語尾に「ござる」を付けてください。"
        )
        dialogue.save()
    return redirect("talk:index")


def samurai(request):
    if request.method == "POST":
        models.Dialogue.objects.all.delete()
        dialogue = models.Dialogue(
            role="system",
            context="今後の返信は語尾に「ござる」を付けてください。"
        )
        dialogue.save()
    return redirect("talk:index")
