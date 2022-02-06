from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View

from .forms import MessageForm
from .models import MessageModel


class IndexView(View):

    method = None
    form: MessageForm = MessageForm
    model: MessageModel = MessageModel

    def get(self, request, method=None):

        return render(request, "dipa_messages/index.html", {"form": self.form})

    def post(self, request, method=None):

        form = self.form(request.POST)
        if form.is_valid():
            self.model.objects.create(
                email=form.cleaned_data["email"], message=form.cleaned_data["message"]
            )
            return render(request, "dipa_messages/success_page.html")
        else:
            return render(
                request, "dipa_messages/error_page.html", {"error_message": form.errors}
            )
