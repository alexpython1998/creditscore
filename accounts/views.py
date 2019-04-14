from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistration
from django import forms
from .models import Question, Choice, UserPolls, Advice
from django.db.models import  Q

BASE_SCORE = 80
# Create your views here.
def home(request):
    return render(request, 'accounts/home.html')


def questions(request):
    question_objs = Question.objects.all()
    # this is a debugger in python
    # import pdb;pdb.set_trace()
    return render(request, 'accounts/questions.html',  {'questions': question_objs})


def submit_polls(request):
    # read logged in user from request
    user = request.user
    # if request.user.is_authenticated:
    #     user is logged in
    print(request.POST)
    # read post paramters from request
    answer1 = request.POST.get('question1')   # 2
    answer2 = request.POST.get('question2')    # 5
    answer3 = request.POST.get('question3')
    answer4 = request.POST.get('question4')
    answer5 = request.POST.get('question5')
    answer6 = request.POST.get('question6')
    choice1 = Choice.objects.get(id=answer1)
    choice2 = Choice.objects.get(id=answer2)
    choice3 = Choice.objects.get(id=answer3)
    choice4 = Choice.objects.get(id=answer4)
    choice5 = Choice.objects.get(id=answer5)
    choice6 = Choice.objects.get(id=answer6)


    score = BASE_SCORE + choice1.score + choice2.score + choice3.score + choice4.score + choice5.score + choice6.score
    UserPolls.objects.create(user=user, score=score)
    # get advice based on score
    user_advices = Advice.objects.filter(Q(min_score__lte=score) & Q(max_score__gte=score))
    return render(request, 'accounts/questions.html', {'score': score, 'user_advices': user_advices})

def registration(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'You are now a UCheck Member! You can now Log In.')
            return redirect('login')
    else:
        form = UserRegistration()
    return render(request, 'accounts/registration.html', {'form': form})