from django.shortcuts import render # type: ignore


def index(request):
    return render(request,'index.html')
def draft_plan(request):
    return render(request, 'draft_plan.html')

