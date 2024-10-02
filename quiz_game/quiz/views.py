from django.shortcuts import render, get_object_or_404
from .models import Question
import random
from django.http import HttpResponse

def quiz(request):
    question = Question.objects.order_by('?').first()
    answers = list(question.answer_set.all())
    random.shuffle(answers)

    if request.method == 'POST':
        selected_answer_id = request.POST.get('answer')
        selected_answer = get_object_or_404(answers, id=selected_answer_id)

        if selected_answer.is_correct:
            return HttpResponse('Correto!')
        else:
            return HttpResponse('Errado!')

    return render(request, 'quiz/quiz.html', {'question': question, 'answers': answers})
