from django.contrib import admin
from django.urls import path
import blogapp.views
import portfolio.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blogapp.views.home, name="home"),
    path('blog/<int:blog_id>',blogapp.views.detail, name="detail"),
    path('blog/new/', blogapp.views.new, name="new"),
    path('blog/create', blogapp.views.create, name="create"),
    #패스를 하나 추가했다고 해서 무조건 html을 띄워야하는 것은 아님
    #create함수를 그냥 실행시키고 싶을 뿐이기에 url을 생성함
    #html을 띄우는 것은 함수의 기능 중 하나일 뿐
    path('portfolio/', portfolio.views.portfolio, name="portfolio"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
