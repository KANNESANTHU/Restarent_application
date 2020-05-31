from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('summernote/', include('django_summernote.urls')),
    path('admin/', admin.site.urls),
    path('', include('firstapp.urls')),
    path('reserve_table/', include('reservation.urls',namespace='reservation')),
    path('blog/', include('blog.urls',namespace='blog')),
    path('aboutus/', include('aboutus.urls',namespace='aboutus')),
    path('contact/', include('contact.urls',namespace='contact')),
    path('home/', include('home.urls',namespace='home')),

]
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header="Restarent adminpanel"