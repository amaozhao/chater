import openai
from django.conf import settings

from .models import Log


class ChatService:
    def __init__(self, api_key=None, *args, **kwargs):
        self.api_key = api_key or settings.OPENAI_KEY

    def chat(self, log, model="gpt-3.5-turbo"):
        profile = log.dialog.user.profile
        if profile.tokens_count <= 0:
            raise 
        # response = openai.ChatCompletion.create(
        #     model=model,
        #     messages=[
        #         {"role": "system", "content": "You are a helpful assistant."},
        #         {"role": "user", "content": log.content},
        #     ],
        #     temperature=0,
        # )
        response = {
            "choices": [
                {
                    "finish_reason": "stop",
                    "index": 0,
                    "message": {"content": "Orange who?", "role": "assistant"},
                }
            ],
            "created": 1679718435,
            "id": "chatcmpl-6xpmlDodtW6RwiaMaC1zhLsR8Y1D3",
            "model": "gpt-3.5-turbo-0301",
            "object": "chat.completion",
            "usage": {"completion_tokens": 3, "prompt_tokens": 39, "total_tokens": 42},
        }
        message = response["choices"][0]["message"]["content"]
        tokens_count = response["usage"]["total_tokens"]
        profile.tokens_count = profile.tokens_count - tokens_count
        profile.save()
        return Log.objects.create(
            dialog=log.dialog,
            content=message,
            source=Log.RESPONSE,
            tokens_count=tokens_count,
        )
