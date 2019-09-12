from django.contrib import admin
from django.urls import path, include
from employee.views import (user_login, success, user_logout, ProfileUpdate, MyProfile)
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('poll.urls')),
    path('employee/', include('employee.urls')),

    path('login/', user_login, name="user_login"),
    path('success/', success, name="user_success"),
    path('logout/', user_logout, name="user_logout"), 
    path('profile/', MyProfile.as_view(), name="my_profile"), 
    path('profile/update/', ProfileUpdate.as_view(), name="profile_update"), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
