import openai
import tiktoken
from django.conf import settings

from .models import Log


class ChatService:
    def __init__(self, api_key=None, *args, **kwargs):
        self.api_key = api_key if api_key else settings.OPENAI_KEY

    def token_count(self, message, model="gpt-3.5-turbo"):
        try:
            encoding = tiktoken.encoding_for_model(model)
        except KeyError:
            encoding = tiktoken.get_encoding("cl100k_base")
        if model == "gpt-3.5-turbo":
            return self.token_count(message, model="gpt-3.5-turbo-0301")
        elif model == "gpt-4":
            print(
                "Warning: gpt-4 may change over time. Returning num tokens assuming gpt-4-0314."
            )
            return self.token_count(message, model="gpt-4-0314")
        elif model == "gpt-3.5-turbo-0301":
            tokens_per_message = 4
            tokens_per_name = -1
        elif model == "gpt-4-0314":
            tokens_per_message = 3
            tokens_per_name = 1
        else:
            raise NotImplementedError(
                f"""num_tokens_from_messages() is not implemented for model {model}. 
                See https://github.com/openai/openai-python/blob/main/chatml.md for information on 
                how messages are converted to tokens."""
            )
        num_tokens = 0
        num_tokens += tokens_per_message
        for key, value in message.items():
            num_tokens += len(encoding.encode(value))
            if key == "name":
                num_tokens += tokens_per_name
        num_tokens += 3
        return num_tokens

    def chat(self, dialoglog, model="gpt-3.5-turbo"):
        # response = openai.ChatCompletion.create(
        #     model=model,
        #     messages=[
        #         {"role": "system", "content": "You are a helpful assistant."},
        #         {"role": "user", "content": dialoglog.content},
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
        log = Log.objects.create(
            dialog=dialoglog.dialog,
            content=message,
            source=Log.RESPONSE,
            tokens_count=tokens_count,
        )
        return log
