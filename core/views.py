from django.shortcuts import render,redirect, get_object_or_404
from core.models import Task
from core.forms import TaskForm

# Create your views here.
def home(request):
    tasks = Task.objects.all()
    return render(request, "todo/page/task_list.html", { "tasks" : tasks})


def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_list')
        return render(request, template_name="todo/page/task_create.html", context={"form": form})
    else:
        form = TaskForm()
        return render(request, template_name="todo/page/task_create.html", context={"form":form})


def task_detail(request, task_pk):
    task = get_object_or_404(Task, id=task_pk)
    return render(request=request, template_name="todo/page/task_detail.html", context={"task": task})

def task_update(request, task_pk):
    task = get_object_or_404(Task,id = task_pk)
    if request.method == "POST":
        form = TaskForm(request.POST, instance = task)
        if form.is_valid():
            form.save()
            return redirect('task_detail', task_pk)
        return render(request=request, template_name="todo/page/task_update.html", context={"form": form})
    else:
        form = TaskForm(instance=task)
        return render(request=request, template_name="todo/page/task_update.html", context={"form": form})
    
def task_delete(request, task_pk):
    task = get_object_or_404(Task,id=task_pk)
    if request.method == "POST":
        task.delete()
        return redirect("task_list")
    return render(request, template_name='todo/page/task_delete.html',context={"task": task} )