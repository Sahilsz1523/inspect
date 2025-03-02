from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordResetView
from .forms import ContactForm, LoginForm
from .forms import VisitorForm
import base64
import uuid
from django.core.files.base import ContentFile
from django.contrib import messages
from .models import Visitor

# Homepage
def index(request):
    return render(request, 'index.html')

# About Us Page
def about_us(request):
    return render(request, 'about_us.html')

# Contact Form
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success")
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})

# Login View



def login_view(request):
    form = LoginForm(request, data=request.POST or None)  # ✅ Pass request for authentication
    
    if request.method == "POST":
        if form.is_valid():  # ✅ Django handles authentication internally
            user = form.get_user()
            login(request, user)
            return redirect("visitor_form")  # ✅ Ensure 'feed' is a valid URL name
        else:
            messages.error(request, "Invalid username or password")

    return render(request, "login_view.html", {"form": form})




    


# Password Reset View
class CustomPasswordResetView(PasswordResetView):
    template_name = "forgot_password.html"
    email_template_name = "password_reset_email.html"
    success_url = reverse_lazy("password_reset_done")

# Feed Form


@login_required
def add_visitor(request):
    if request.method == "POST":
        name = request.POST["name"]
        phone = request.POST["phone"]
        address = request.POST["address"]
        email = request.POST["email"]
        description = request.POST["description"]
        id_proof_data = request.POST.get("id_proof_data")

        image_data = None
        if id_proof_data:
            format, imgstr = id_proof_data.split(";base64,")
            ext = format.split("/")[-1]
            image_data = ContentFile(base64.b64decode(imgstr), name=f"{uuid.uuid4()}.{ext}")

        # Save visitor and link to logged-in user
        visitor = Visitor(
            user=request.user,
            name=name,
            phone=phone,
            address=address,
            email=email,
            description=description,
            id_proof=image_data
        )
        visitor.save()

        return redirect("visitor_form")  # Redirect to visitor list

    return render(request, "visitor_form.html")


 # Load the form page
@login_required
def visitor_list(request):
    visitors = Visitor.objects.filter(user=request.user)  # Show only current user's visitors
    return render(request, "visitor_list.html", {"visitors": visitors})
# Success Page
def success(request):
    return render(request, "success.html")
