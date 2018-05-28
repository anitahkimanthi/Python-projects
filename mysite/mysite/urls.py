from django.conf.urls import include,url
from django.contrib import admin

urlpatterns = [
	url(r'^polls/', include('polls.urls')),
	# url(r'^Questions/', include('Questions.urls')),
	url(r'^admin/', admin.site.urls)
]