from django.shortcuts import render, redirect
import openai
from tenacity import retry, stop_after_attempt, wait_random_exponential
from time import sleep
from textblob import TextBlob
from django.contrib.auth import authenticate, login
from django.contrib import messages as msgs


# Chat GPT Completion - takes only messages param as structured prompt
@retry(wait=wait_random_exponential(multiplier=1, max=60), stop=stop_after_attempt(8))
def chatgpt_completion(messages, model="gpt-3.5-turbo"):
    # TODO: Prompt builder function - house in prompt_funcs.py
    prompt = [
        {
            "role": "system",
            "content": "I am an intelligent artificial cognitive entity (acog) named JULIET. I "
                       "am helpful, friendly, polite and always conduct myself professionally. "
        },
        {
            "role": "user",
            "content": messages
        },
        {
            "role": "assistant",
            "content": ""
        },
    ]
    response = openai.ChatCompletion.create(model=model, messages=prompt)
    text = response['choices'][0]['message']['content']

    return text


# Vectorize with OpenAI GPT Embeddings (1,536 dimensions - Pinecone?)
@retry(wait=wait_random_exponential(multiplier=1, max=60), stop=stop_after_attempt(8))
def gpt_embedding(content, engine='text-embedding-ada-002'):
    # fix any UNICODE errors
    content = content.encode(encoding='ASCII', errors='ignore').decode()

    while True:
        try:

            # create the embedding
            response = openai.Embedding.create(
                input=content,
                engine=engine)
            # vectorize the embedding and return it
            vector = response['data'][0]['embedding']
            return vector

        except Exception as oops:
            print('Error communicating with OpenAI embeddings:', oops)
            sleep(1)


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate the User
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            msgs.success(request, f'Hi, {username}! You are now logged in.')
            return redirect('index.html')
        else:
            msgs.success(request, "There was an error logging you in. Please try again.")

    return render(request, 'login.html', {})


def logout_user(request):
    return render(request, 'index.html')


def analyze_sentiment(corpus):
    text_blob = TextBlob(corpus)
    sentiment = text_blob.sentiment
    return sentiment


# Create your views here.
def index(request):
    return render(request, 'index.html')


def account_profile(request):
    return render(request, 'account-profile.html')


def base(request):
    return render(request, 'base.html')


def chat(request):
    return render(request, 'chat.html')


def overview(request):
    return render(request, 'overview.html')


def blog_main(request):
    return render(request, 'blog.html')


def education_main(request):
    return render(request, 'education.html')


def creators_main(request):
    return render(request, 'creators.html')


def signup(request):
    return render(request, 'signup.html')


def site_terms(request):
    return render(request, 'terms-of-service.html')


def privacy_policy(request):
    return render(request, 'privacy-policy.html')


def account_security(request):
    return render(request, 'account-security.html')


def account_notifications(request):
    return render(request, 'account-notifications.html')


def open_ai_chat(request):
    return render(request, 'gpt-4_chat-bot.html')