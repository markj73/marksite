
from libs.views.hybrid import *
from libs.utils.urlresolvers import *
from apps.todo.models import TodoItem
from apps.todo.forms import TodoItemForm
# Create your views here.
class IndexView(LoginHybridListView):
    model = TodoItem
    template_name = 'todo/index.html'
    context_object_name = 'todolist'
    
    def get_queryset(self):
        """
        Get the list of items for this view.
        """
        items = self.model._default_manager.filter(user=self.request.user, finished=False)

        def getScore( anObject ):
            return anObject.score()
        objects= list(items)
        objects.sort( key=getScore, reverse=True )
        #items = queryset.filter(user=self.request.user)
        return objects

class TodoItemUpdateView(LoginHybridUpdateView):    
    model = TodoItem
    form_class = TodoItemForm
    template_name = 'todo/detail.html'
    context_object_name = 'item'
    success_url = '/todo/'

    def form_valid(self, form):
        """
        Validate and save the form
        """
        user = self.request.user
        self.object = form.save(user)
        return super(TodoItemUpdateView, self).form_valid(form)

class TodoItemCreateView(LoginHybridCreateView):    
    model = TodoItem
    form_class = TodoItemForm
    template_name = 'todo/detail.html'
    context_object_name = 'item'
    success_url = '/todo/'

    def form_valid(self, form):
        """
        Validate and save the form
        """
        user = self.request.user
        self.object = form.save(user)
        return super(TodoItemCreateView, self).form_valid(form)

    