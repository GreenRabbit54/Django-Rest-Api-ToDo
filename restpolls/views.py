from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from restpolls.models import Poll


def polls_list(request):
    MAX_OBJECTS = 20
    polls = Poll.objects.all()[:MAX_OBJECTS]
    data = {'result':list(polls.values('question','pub_date','created_by'))}
    return JsonResponse(data)


def polls_detail(request, pk):
    poll = get_object_or_404(Poll,pk)
    data = {'result':{
        'question': poll.question,
        'pub_date':poll.pub_date,
        'created_by':poll.created_by,

    }}
    return JsonResponse(data)