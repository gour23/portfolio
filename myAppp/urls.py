from django.contrib import admin
from django.urls import path,include
from myAppp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.home,name="home"),
    path('work/',views.work,name="work"),
    path('contact/',views.contact,name="contact"),
    path('achievments/',views.achievments,name="achivements"),
    path('workposts/<str:slug>', views.workposts, name='workposts'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)