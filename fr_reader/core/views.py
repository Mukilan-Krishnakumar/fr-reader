from django.shortcuts import render
from django.http import JsonResponse
from core.forms import TranslateForm
from core.actions.translate_actions import TranslateSourceAction


# Create your views here.
def health(request):
    return JsonResponse({"success": "true"}, status=200)


def translate_site(request):
    if request.method == "POST":
        form = TranslateForm(request.POST)
        if form.is_valid():
            TranslateSourceAction(url=form.cleaned_data["url"]).execute()
    else:
        form = TranslateForm()
    return render(request, "core/home.html", {"form": form})
