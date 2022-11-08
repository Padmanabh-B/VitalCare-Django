from django.contrib import admin
from .models import HeadCard,Card,Emergency,About,Services,Contact
# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display=('id','fname','address','email','phone')
    search_fields=('address',)
    list_filter=('address',)



admin.site.register(HeadCard)
admin.site.register(Card)
admin.site.register(Emergency)
admin.site.register(About)
admin.site.register(Services)
admin.site.register(Contact,ContactAdmin)
