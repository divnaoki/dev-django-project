from pydoc import render_doc
from certifi import contents
from django.shortcuts import render
from .models import Todo
from .forms import CreateTodoForm
# Create your views here.
def index_view(request):
  items = Todo.objects.all()
  contents = {
    'items': items
  }
  return render(request, 'todo/index.html', contents)

def create_view(request):
  form = CreateTodoForm()
  if request.method == "POST":
    form = CreateTodoForm(request.POST)
  context = {
    "form": form
  }
  return render(request, "todo/create.html", context)