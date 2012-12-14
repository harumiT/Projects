#from django.template import Context, loader 
from django.shortcuts import render_to_response, get_object_or_404
from polls.models import Poll, Choice
from django.http import HttpResponseRedirect#, Http404, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext

def index(request):
    poll_list = Poll.objects.all().order_by('-pub_date')[:5]
    #t = loader.get_template('polls/index.html')
    #c = Context({
    #             'latest_poll_list': poll_list, # 'latest_poll_list' is the object that will used in the HTML
    #})
    #return HttpResponse(t.render(c))
    return render_to_response('polls/index.html', {'latest_poll_list': poll_list}) # it's a different way to implement, using shortcut (atalho). Using this way, you don't need to import the context, loader and HttpResponse

def detail(request, poll_id, name):
    #try:
    #    p = Poll.objects.get(pk = poll_id)
    #except Poll.DoesNotExist:
    #    raise Http404
    #return render_to_response()('polls/detail.html', {'poll': p})
    p = get_object_or_404(Poll, pk = poll_id)
    return render_to_response('polls/detail.html', {'poll': p, 'name': name}, context_instance=RequestContext(request))

def results(request, poll_id):
    p = get_object_or_404(Poll, pk = poll_id)
    return render_to_response('polls/results.html', { 'poll': p })

def vote(request, poll_id):
    p = get_object_or_404(Poll, pk = poll_id)
    
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render_to_response('polls/detail.html', { 'poll': p, 
                                                        'error_message': 'You didn\'t select a choice' 
                                                      },
                                                      context_instance = RequestContext(request))
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing with POST data.
        # This prevents data from being posted twice if a user hits the Back button.
        return HttpResponseRedirect(reverse('polls.views.results', args = (p.id,)))