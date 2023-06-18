from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.utils import timezone
from .models import Chat
from .utils import chat_openai_helper_function

from django.contrib.auth.decorators import login_required


@login_required
def chats(request):
    chats = Chat.objects.filter(user=request.user)
    recentChats = Chat.objects.filter(user=request.user).order_by("-created_at")[
        :10
    ]  # Fetch the last 10 chat conversations

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

    recent_chats = [
        {"message": chat.message, "response": chat.response} for chat in recentChats
    ]

    context = {
        "recent_chats": recent_chats,
        "chats": chats,
    }
    return render(request, "chats/chat_page.html", context)


@login_required
def clear_chats(request):
    Chat.objects.filter(user=request.user).delete()
    return redirect("chats")  # Redirect back to the chat page after clearing the chats
