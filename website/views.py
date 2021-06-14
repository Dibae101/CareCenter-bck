from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail, EmailMessage
from rootlevel.settings import EMAIL_HOST_USER
from django.http import HttpResponse
from .forms import ResumeForm
from .models import Resume
from django.views import View

# Create your views here.


def home(request):
    return render(request, "home.html")


def contact(request):
    if request.method == "POST":
        message_name = request.POST["message-name"]
        message_email = request.POST["message-email"]
        message = request.POST["message"]
        # send email
        send_mail(
            message_name,
            message,
            message_email,
            ["example@gmail.com"],
            fail_silently=False,
        )
        return render(request, "contact.html", {"message_name": message_name})
    else:
        return render(request, "contact.html")


# def send_email(request):
#     if request.method == "POST":
#         message = request.POST.get("message", "")
#         subject = request.POST.get("subject", "")
#         mail_id = request.POST.get("email", "")
#         email = EmailMessage(subject, message, EMAIL_HOST_USER, [mail_id])
#         email.content_subtype = "html"
#         file = request.FILES["file"]
#         email.attach(file.name, file.read(), file.content_type)
#         email.send()

#         return render(request, "carrer.html", {"message": message})
#     else:
#         return render(request, "carrer.html")


def services(request):
    return render(request, "services.html")


def about(request):
    return render(request, "about.html")


def tour(request):
    return render(request, "tour.html")


# def carrer(request):
#     return render(request, "carrer.html")

class HomeView(View):
    def get(self, request):
        form = ResumeForm()
        return render(request, 'carrer.html',  {'form': form})

    def post(self, request):
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            from django.contrib import messages
            messages.success(request, 'Profile details updated.')
            return render(request, 'carrer.html', {'form': form})
        else:
            return render(request, 'carrer.html', {'form': form})