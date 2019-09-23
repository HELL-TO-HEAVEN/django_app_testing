from django.shortcuts import get_object_or_404, render

# Create your views here.

def index(request):
    question_list = [1,2,3,4,5]
    context = {'question_list': question_list}
    return render(request, 'analyze/index.html', context)
