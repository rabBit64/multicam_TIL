from django.shortcuts import render,redirect
from .models import Todo
from .forms import TodoForm

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
        'todo': todo,
    }
    return render(request,'detail.html', context)

def new(request):
    form = TodoForm()
    context = {
        'form':form,
    }
    return render(request, 'new.html',context)

def create(request):
    '''
    print(request.GET.get('title'))
    title = request.POST.get('title')
    content = request.POST.get('content')
    priority = request.POST.get('priority')
    deadline = request.POST.get('deadline')
    # DB 저장
    todo = Todo(title=title,content=content,priority=priority,deadline=deadline)
    todo.save()
    '''
    
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save()
            #이동할 url 응답
            return redirect("todos:detail", todo.pk)
        context = {
            'form':form,
        }
        return render(request,'new.html', context)
    else:
        form = TodoForm()
        context = {
            'form':form,
        }
        return render(request,'todos:new.html', context)
    #return render(request, 'create.html')

def update(request,todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    if request.method == 'POST':
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('todos:detail', todo.pk)
    else:
        form = TodoForm(instance=todo)
    context = {
        'todo': todo,
        'form': form,
    }
    return render(request, 'edit.html', context)

def delete(request, todo_pk):
    todo = Todo.objects.get(pk=todo_pk)
    todo.delete()
    return redirect('todos:index')

def edit(request):  
    return render(request, 'edit.html')
