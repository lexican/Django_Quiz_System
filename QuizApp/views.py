from django.shortcuts import render, get_object_or_404
from .models import Quiz, Scores
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from . import calculate


@login_required(login_url='/login/')
def index(request):
    quiz = Quiz.objects.all()
    paginator = Paginator(quiz, 1)  # Show 1 contacts per page
    page = request.GET.get('page')
    quiz = paginator.get_page(page)

    if request.method == 'POST':
        answer = request.POST['choice']
        quiz_id = request.POST['quiz_id']
        quiz_check = get_object_or_404(Quiz, pk=int(quiz_id))
        ans = quiz_check.answer
        if quiz_check.answer == answer:
            calculate.answer(quiz_id, 1)
        else:
            calculate.answer(quiz_id, 0)
        data = [{'message': "Response received", 'ans': ans}]
        return JsonResponse(data, safe=False)

    context = {
        'quiz': quiz
        }

    return render(request,"index.html", context)


def submit(request):
    score = calculate.showresult()
    q = Scores(user=request.user, score=score)
    # Save the object into the database. You have to call save() explicitly.
    q.save()
    context = {
        'score': score,
        'message': "Thank you!",
    }
    return render(request, 'result.html', context)







