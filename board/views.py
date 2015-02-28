from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.views import generic

from board.models import Todo, InProgress, Finished

def IndexView():
    template_name = 'board/index.html'
    Todo.objects.order_by('-pub_date')[:5]
    return render()

class InProgressView(generic.DetailView):
    model = InProgress
    template_name = 'board/InProgress.html'

def FinishedView(request, Finished_id):
    p = get_object_or_404(InProgress, pk=Finished_id)
    try:
         selected = p.get(pk=request.POST['In Progress'])
    except (KeyError, p.DoesNotExist):
        return render(request, 'board/finished.html', {
            'InProgress': p,
            'error_message': "This isn't a valid choice",
        })
    else:
        print selected

    return HttpResponse(response % Finished_id)



