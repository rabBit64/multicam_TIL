from django.shortcuts import render,redirect
from .models import Todo

def index(request):
     # 전체게시글 조회 (결과가 쿼리셋으로 옴)
    todos = Todo.objects.all()
    print(todos)
    context = {
        'articles':todos,
    }
        
    return render(request,'index2.html',context)

def detail(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    print(todo)
    context = {
        'article': todo,
    }
    return render(request,'detail.html', context)

def new(request):
    return render(request, 'new.html')

def create(request):
    print(request.GET.get('title'))
    title = request.GET.get('title')
    content = request.GET.get('content')
    priority = request.GET.get('priority')
    deadline = request.GET.get('deadline')


    # DB 저장
    todo = Todo(title=title,content=content,priority=priority,deadline=deadline)
    todo.save()
    #return render(request, 'create.html')

    #이동할 url 응답
    return redirect("todos:index")

def delete(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    todo.delete()
    return redirect('todos:index')

def edit(request):
    return render(request, 'edit.html')
