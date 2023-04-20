from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import UserProfile
from memory_graph.models import Person, Place, RelationshipPersonPerson, RelationshipPersonPlace

# Unregister Group model from admin.
admin.site.unregister(Group)


# Mix Profile model into User model
class ProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = "profile"


# Extend User Model
class UserAdmin(admin.ModelAdmin):
    model = User
    # Only display username fields on admin page
    fields = ["username", "email", "first_name", "last_name"]
    inlines = [ProfileInline]


# Unregister initial user model from admin
admin.site.unregister(User)

# Re-register user model with new UserAdmin
admin.site.register(User, UserAdmin)
# admin.site.register(UserProfile)
admin.site.register(Person)
admin.site.register(Place)
admin.site.register(RelationshipPersonPerson)
admin.site.register(RelationshipPersonPlace)
