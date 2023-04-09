import openai
import tiktoken
from django.conf import settings


class ChatService:
    def __init__(self, api_key=None, *args, **kwargs):
        self.api_key = api_key if api_key else settings.OPENAI_KEY

    def token_count(self, message, model="gpt-3.5-turbo-0301"):
        try:
            encoding = tiktoken.encoding_for_model(model)
        except KeyError:
            encoding = tiktoken.get_encoding("cl100k_base")
        if model == "gpt-3.5-turbo":
            return self.token_count(message, model="gpt-3.5-turbo-0301")
        elif model == "gpt-4":
            print("Warning: gpt-4 may change over time. Returning num tokens assuming gpt-4-0314.")
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
                how messages are converted to tokens.""")
        num_tokens = 0
        num_tokens += tokens_per_message
        for key, value in message.items():
            num_tokens += len(encoding.encode(value))
            if key == "name":
                num_tokens += tokens_per_name
        num_tokens += 3
        return num_tokens

    def chat(self, request, model="gpt-3.5-turbo"):
        completion = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": "Hello world!"}]
        )
        print(completion.choices[0].message.content)
