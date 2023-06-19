from django.shortcuts import render
from . import forms

# Create your views here.
def index(request):
    form = forms.ChatForm()
    if request.method == "POST":
        user_message = "Your message:" + request.POST["message"]
        chatgpt_message = "ChatGPT message:" + "ChatGPTの返信を代入する"
    else:
        user_message = "{何も入力されていません}"
        chatgpt_message = "{何も入力されていません}"
    context = {
        "form": form,
        "user_message": user_message,
        "chatgpt_message": chatgpt_message
    }
    return render(request, 'talk/index.html', context)
