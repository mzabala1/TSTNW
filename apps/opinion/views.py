from django.shortcuts import render, redirect
from .forms import OpinionForm
from .models import Opinion
from django.contrib.auth import get_user
from django.contrib.auth.decorators import login_required


@login_required
def opinion_view(request):
    form = OpinionForm(request.POST)
    if form.is_valid():
        form.escritor = request.user.username
        if request.method == 'POST':
            form.save()
        return redirect('OpinionApp:Opiniones')

    return render(request, 'opinion/opinion.html', {'form': form})


def opiniones_list(request):
    opinion = Opinion.objects.all()
    contexto = {'opiniones': opinion}

    return render(request, 'opinion/opinion_list.html', contexto)
