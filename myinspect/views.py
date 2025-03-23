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

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message has been sent successfully!")
            form = ContactForm()  # Reset the form after submission
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


import base64
import uuid
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.files.base import ContentFile
from django.contrib.auth.decorators import login_required
from .models import Visitor  # Import your Visitor model

@login_required
def add_visitor(request):
    if request.method == "POST":
        try:
            name = request.POST["name"]
            phone = request.POST["phone"]
            address = request.POST["address"]
            email = request.POST["email"]
            description = request.POST["description"]
            id_proof_data = request.POST.get("id_proof_data", None)

            # Handle image data
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

            messages.success(request, "Visitor details submitted successfully!")
            return redirect("visitor_form")  # Redirect to prevent duplicate form submission

        except Exception as e:
            messages.error(request, "An error occurred while submitting the form.")

    return render(request, "visitor_form.html")


 # Load the form page
@login_required
def visitor_list(request):
    query = request.GET.get('search', '')  # Get search query from request
    visitors = Visitor.objects.filter(user=request.user).order_by('-date_time')

    if query:
        visitors = visitors.filter(name__icontains=query)  # Filter by visitor name

    # Format the date before sending it to the template
    for visitor in visitors:
        visitor.formatted_date = visitor.date_time.strftime("%b %d, %Y %I:%M %p")  

    return render(request, "visitor_list.html", {"visitors": visitors, "search_query": query})
