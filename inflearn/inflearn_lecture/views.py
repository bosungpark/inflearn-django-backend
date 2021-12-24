from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate, login
from .models import myText, Comment
from .forms import LectureForm

def home_list(request):
    texts=myText.objects.filter()

    return render(request, 'inflearn_lecture/home_list.html',{'texts':texts})

def lecture_list(request):
    texts=myText.objects.filter()
    hot_lecture=myText.objects.filter(category="인기 강의")
    return render(request, 'inflearn_lecture/lecture_list.html',
    {'texts':texts, 'hot_lecture':hot_lecture})

def login(request):

    if request.method == 'POST':

        email=request.POST.get('email')
        pwd=request.POST.get('pwd')

        user=auth.authenticate(request,username=email,passward=pwd)
        print(user)
        if user is not None:         
            auth.login(request,user)
            return redirect('/')
        else:
            return redirect('/join')

    return render(request, 'inflearn_lecture/login.html')

def join(request):
    
    if request.method=='POST':

        email=request.POST['email']
        pwd=request.POST['pwd']
        
        User.objects.create_user(username=email,password=pwd)

        return redirect('/')

    return render(request, 'inflearn_lecture/join.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def lecture_list_info(request,pk):

    board_contents=get_object_or_404(myText, pk=pk)
    comment=Comment.objects.filter(lecture=board_contents)

    if request.method=='POST':
        rate=request.POST['rate']
        writer=request.POST['writer']
        comment=request.POST['comment']

        Comment.objects.create(lecture=board_contents,
                                writer=writer,
                                rate=rate,
                                comment=comment,
                                )
        return redirect('/lecture_list/'+str(pk))
    
    return render(request, 'inflearn_lecture/lecture_list_info.html',
                    {'board_contents':board_contents,
                    'comment':comment,
                    })

def comment_remove(request,pk):

    if request.method=='post':
        Comment.objects.get(pk=pk).delete()
    
    return redirect('/lecture_list')

def show_lecture(request,pk):

    board_contents=get_object_or_404(myText,pk=pk)

    return render(request, 'inflearn_lecture/show_lecture.html',{'board_contents':board_contents})

def create_lecture(request):

    if request.method=='POST':
        form=LectureForm(request.POST, request.FILES)
        if form.is_valid():
            myText=form.save(commit=False)
            myText.author=request.user
            myText.save()
            return redirect('/')


    lecture_form=LectureForm()

    return render(request, 'inflearn_lecture/create_lecture.html', {'lecture_form':lecture_form})

def my_lecture(request):

    lectures=myText.objects.filter(author=request.user)

    return render(request, 'inflearn_lecture/my_lecture.html', {'lectures':lectures})

def edit_my_lecture(request, pk):

    lecture=get_object_or_404(myText,pk=pk)
    
    if request.method=='POST':
        form=LectureForm(request.POST, request.FILES, instance=lecture)
        if form.is_valid():
            lecture=form.save(commit=False)
            lecture.author=request.user
            lecture.save()

            return redirect('/my_lecture')
    else:
        form=LectureForm(instance=lecture)

    return render(request, 'inflearn_lecture/edit_my_lecture.html',{'lecture_form':form,'primary_key':pk})
