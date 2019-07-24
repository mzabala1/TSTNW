from django.shortcuts import render, redirect
# from .forms import OpinionForm


def opinion_view(request):
    form = OpinionForm(request.POST)
    if form.is_valid():
        if request.method == 'POST':
            form.save()
        return redirect('OpinionApp:opinion')

    return render(request, 'opinion/opinion.html', {'form': form})