from django.shortcuts import render, get_object_or_404


def chats(request):
    return render(request, "chats/chat_page.html")
