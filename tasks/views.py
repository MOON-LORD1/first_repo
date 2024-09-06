from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Task, Profile, Answer
from .forms import AnswerForm, LoginForm, PfpForm
from django.contrib.auth import authenticate, login, logout
import random  
import re 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import F

# Create your views here.
def main_view(req):
    user = req.user

    all_tasks = Task.objects.all()
    latest_task = all_tasks.order_by('-id')[0]
    latest_tasks = all_tasks.order_by('-id')[:8]
    random_tasks = []
    
    id_list = random.sample(list(all_tasks.values_list('id', flat=True)), len(all_tasks))
    new_random_task = random.choice(all_tasks)

    # answer = Answer.objects.all()



    for i in id_list:
        random_tasks.append(all_tasks[i - 1])
        
    random_tasks = random_tasks[:8]
    obj = {
        'all_tasls': all_tasks,
        'latest_task': latest_task,
        'latest_tasks': latest_tasks,
        'random_tasks': random_tasks,
        'user': user,
        'new_random_task': new_random_task,
        # 'answer': answer,
    }

    if user.is_authenticated:
        if req.method == "POST":
            form = PfpForm(req.POST, req.FILES)

            if form.is_valid():
                update_profile = Profile.objects.get(user=req.user)
                update_profile.pfp = req.FILES['pfp']
                update_profile.save()

                return redirect('/')
            else:
                return HttpResponse('error')
        else:
            form = PfpForm()
            profile = Profile.objects.get(user=user)
            obj['profile'] = profile
            obj['form'] = form
            return render(req, "main.html", obj)
    else:
        return render(req, "unauth.html", obj)


def skip_task(req):
    all_tasks = Task.objects.all()
    new_random_task = random.choice(all_tasks)

    obj = {
        'new_random_task': new_random_task,
        'user': req.user,
    }

    return render(req, "main.html", obj)



# def solve_view(req, pk):
#     task = Task.objects.get(id=pk)
#     user = req.user
#     answer = Answer.objects.all().filter(author=user, task=task).order_by('-id')
#     obj = {'task': task, 'answer': answer}

#     if answer:
#         obj['answer'] = answer


#     return render(req, 'solve.html', obj)




@login_required(login_url='login')  # Укажите свой URL-путь для главной страницы, если пользователь не аутентифицирован
def solve_view(request, pk):
    # Оставьте остальной код как есть
    task = Task.objects.get(id=pk)
    user = request.user
    answer = Answer.objects.filter(author=user, task=task).order_by('-id')

    

    if request.method == 'POST':
        code = request.POST.get('code', '')
        # Answer.objects.create(author=user, task=task, code=code, stat="На проверке")
        answer = Answer.objects.create(author=user, task=task, code=code, stat="На проверке")
    
        def answer_is_correct(answer):
                return answer.stat == "Все верно"

        if answer_is_correct(answer):
        # Обновляем значение solved_problems для пользователя
            Profile.objects.filter(user=user).update(solved_problems=F('solved_problems') + 1)
        return redirect('solve', pk=pk)

    obj = {'task': task, 'answer': answer}
    return render(request, 'solve.html', obj)


# @login_required(login_url='login')
# def solve_view(request, pk):
#     task = Task.objects.get(id=pk)
#     user = request.user

#     if request.method == 'POST':
#         code = request.POST.get('code', '')
#         # Создаем запись в модели Answer
#         answer = Answer.objects.create(author=user, task=task, code=code, stat="На проверке")
#         def answer_is_correct(answer):
#             return answer.stat == "Все верно"
#         # Проверяем, верное ли решение предоставил пользователь
#         if answer_is_correct(answer):
#             # Обновляем значение solved_problems для пользователя
#             Profile.objects.filter(user=user).update(solved_problems=F('solved_problems') + 1)

#         return redirect('solve', pk=pk)

#     obj = {'task': task}
#     return render(request, 'solve.html', obj)



def login_view(req):
    if req.method == 'POST':
        form = LoginForm(req.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])

            if user != None:
                if user.is_active:
                    login(req, user)
                    return redirect('/login-success')
                else:
                    messages.error(req, 'Аккаунт неактивен')
            else:
                messages.error(req, 'Неправильный логин или пароль')
                return redirect('/login')
    else:
        form = LoginForm()
    
    return render(req, 'login.html', {'form': form})

def login_succes_view(req):
    return render(req, 'login-success.html', {})

def logout_view(req):
    logout(req)
    return render(req, 'logout.html', {})


# def user_log(req, log):
#     return render(req, 'user_log.html')


def account_log(request, username):
    user = request.user
    if user.is_authenticated:
        user_email = user.email
        return render(request, 'account_log.html', {'user': user, 'email': user_email})
    else:
        return Http404()

