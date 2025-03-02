from django.contrib import admin
from .models import Visitor  # Import the feed model


 # Prevent editing of creation date
from .models import Contact
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created_at")
    search_fields = ("name", "email")
    list_filter = ("created_at",) 

from django.contrib import admin
from .models import Visitor


class VisitorAdmin(admin.ModelAdmin):
    list_display = ["name", "phone", "address", "email", "date_time", "user"]  # Added user field
    search_fields = ["name", "phone", "email"]  # Allow searching by name, phone, email
    list_filter = ["date_time"]  # Allow filtering by date
    ordering = ["-date_time"]  # Show the latest visitors first

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs  # Superusers see all visitors
        return qs.filter(user=request.user)  # Normal users see only their own visitors

    def has_change_permission(self, request, obj=None):
        if not request.user.is_superuser and obj and obj.user != request.user:
            return False  # Prevents normal users from editing others' visitors
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        if not request.user.is_superuser and obj and obj.user != request.user:
            return False  # Prevents normal users from deleting others' visitors
        return super().has_delete_permission(request, obj)

admin.site.register(Visitor, VisitorAdmin)



# Register your models here.
