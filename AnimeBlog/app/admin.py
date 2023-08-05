from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from app.models import Account, BlogPost
# Register your models here.



class AccountAdmin(UserAdmin):
	list_display = ('email','name','username','date_joined', 'last_login', 'is_admin','is_staff')
	search_fields = ('email','name','username',)
	readonly_fields=('id', 'date_joined', 'last_login')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()


admin.site.register(Account, AccountAdmin)
admin.site.register(BlogPost)