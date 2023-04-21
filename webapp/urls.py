from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("profile/", views.user_profile, name="user_profile"),

    path("base/", views.base, name="base"),
    path("chat/", views.chat, name="chat"),
    path("overview/", views.overview, name="overview"),
    path("blog/", views.blog_main, name="blog"),
    path("education/", views.education_main, name="education"),
    path("creators/", views.creators_main, name="creators"),
    path("signup/", views.signup, name="signup"),
    path("terms-of-service/", views.site_terms, name="terms_of_service"),
    path("privacy-policy/", views.privacy_policy, name="privacy_policy"),
    path("open-ai-chat/", views.open_ai_chat, name="open_ai_chat"),
    path("what-we-do/", views.what_we_do, name="what_we_do"),

    path("jotter/", views.jotter, name="jotter"),
    path("jotter_profiles/", views.profile_list, name="jotter_profiles"),

]
