"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mysite import views  # import views

# This is STEP 1 for file uploadtion
# When working with media we have to import below two libraries
from django.conf import settings
from django.conf.urls.static import static
# For STEP 3 visit buttom of this page

urlpatterns = [
    path('main-admin/', admin.site.urls),
    path('', views.homepage, name="home"),
    path('blog/', views.blog, name="blog"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    # path('submitdata/', views.submitdata, name="submitdata"),
    path('submitMarks/', views.submitMarks, name="submitMarks"),
    path('marksheet/', views.marksheet, name="marksheet"),
    path('news/', views.news, name="newsUrl"),
    path('newsUrl/<newsSlug>', views.newsUrl)




    # path('courses/', views.courses),
    # path('blog/<slug:courseId>', views.courseDetail), # For slug
    # path('courses/<int:courseId>', views.courseDetail), For int
    # path('courses/<str:courseId>', views.courseDetail), for str
    # path('courses/<courseId>', views.courseDetail), when we don't know the type
]


# This is STEP 3 for file uploadtion
# When working with media include below line of code
# Here we are giving permission to access media directory
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
# Now the basic settings are done, you can go ahead and create a File feild in your models.py