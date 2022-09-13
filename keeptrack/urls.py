"""
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from account import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_page,name='home-page'),
    
    path('skill/',include('skill.urls')),
    path('project/',include('project.urls')),
    path('account/',include('account.urls')),
    
]

urlpatterns+= static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)