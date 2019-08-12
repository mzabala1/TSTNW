from django.shortcuts import render, redirect
from .forms import OpinionForm
from .models import Opinion
from .serializers import OpinionSerializer
from rest_framework import generics
from django.contrib.auth.decorators import login_required


@login_required
def opinion_view(request):
    form = OpinionForm(request.POST)
    if form.is_valid():
        form = form.save(commit=False)
        form.escritor = request.user
        if request.method == 'POST':
            form.save()
        return redirect('OpinionApp:Opiniones')

    return render(request, 'opinion/opinion.html', {'form': form})


def opiniones_list(request):
    opinion = Opinion.objects.all()
    contexto = {'opiniones': opinion}

    return render(request, 'opinion/opinion_list.html', contexto)


class OpinionesRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk' #id
    serializer_class = OpinionSerializer
    queryset = Opinion.objects.all()


class OpinionesFullList(generics.ListAPIView):
    lookup_field = 'pk' #id
    serializer_class = OpinionSerializer
    queryset = Opinion.objects.all()
