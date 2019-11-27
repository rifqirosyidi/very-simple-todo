from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
from main.models import Todo
from django.http import HttpResponseRedirect

# Create your views here.
def home(request):
    todo_lists = Todo.objects.all().order_by('-added_date')
    context = {
      'todo_lists': todo_lists
    }
    return render(request, 'main/index.html', context)

@csrf_exempt
def add_todo(request):
  added_date = timezone.now()
  content = request.POST.get('content')
  todo = Todo.objects.create(added_date=added_date, content=content)
  print(todo)
  return HttpResponseRedirect('/')


def del_todo(request, todo_id):
  Todo.objects.get(id=todo_id).delete()
  return HttpResponseRedirect('/')