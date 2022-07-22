from django.contrib import admin
from first_app.models import Topic, Webpage, AccessRecord, UserInfo

# Register your models here.
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(AccessRecord)
admin.site.register(UserInfo)