from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.utils import timezone
from .models import Chat
from .utils import chat_openai_helper_function


def chats(request):
    chats = Chat.objects.filter(user=request.user)

    if request.method == "POST":
        message = request.POST.get("message")
        response = chat_openai_helper_function(message)

        chat = Chat(
            user=request.user,
            message=message,
            response=response,
            created_at=timezone.now(),
        )
        chat.save()
        return JsonResponse({"message": message, "response": response})

    context = {"chats": chats}
    return render(request, "chats/chat_page.html", context)
