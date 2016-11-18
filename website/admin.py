from django.contrib import admin

# Register your models here.
from .models import ContactUs, ContentManagement, ContactStatus


#class SiteAdmin(admin.ModelAdmin):



#models = [ContactUs, ContentManagement]
#admin.site.register(models)

admin.site.register(ContactUs)


admin.site.register(ContentManagement)

admin.site.register(ContactStatus)

admin.site.site_header = "Ecclesiastes Site Management Tool"