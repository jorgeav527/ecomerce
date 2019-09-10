from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('core.urls', namespace='core')),
]

admin.site.site_header = 'Ecomerce Admin'       # default: "Django Administration"
admin.site.index_title = 'Ecomerce Admin List'  # default: "Site administration"
admin.site.site_title = 'Ecomerce Title'        # default: "Django site admin"
