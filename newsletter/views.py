from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import SignUpForm, ContactForm


# Create your views here.
def home(request):
    title = 'Welcome'
    form = SignUpForm(request.POST or None)

    context = {
        "title": title,
        "form": form,
    }

    if form.is_valid():
        instance = form.save(commit=False)

        full_name = form.cleaned_data.get("full_name")
        if not full_name:
            full_name = "New full name"
        instance.full_name = full_name
        # if not instance.full_name:
        #     instance.full_name = "youhan"
        instance.save()
        print(instance.timestamp)
        context = {
            "title": "Thank you"
        }

    return render(request, "home.html", context)

def contact(request):
    title = "Contact Us Anytime!"
    title_align_center = True
    form = ContactForm(request.POST or None)
    if form.is_valid():
        # for key, value in form.cleaned_data.items():
        #     print(key, value)
            # print(form.cleaned_data.get(key))
        form_email = form.cleaned_data.get("email")
        form_message = form.cleaned_data.get("message")
        form_full_name = form.cleaned_data.get("full_name")
        # print(email, message, full_name)
        subject = 'Site contact form'
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email, "youhanlee@kaist.ac.kr"]
        contact_message = "{}: {} via {}".format(form_full_name, form_message, form_email)
        send_mail(subject,
                  contact_message,
                  from_email,
                  to_email,
                  fail_silently=False )
    context = {
        "title": title,
        "form": form,
        "title_align_center": title_align_center,
    }
    return render(request, "forms.html", context)











