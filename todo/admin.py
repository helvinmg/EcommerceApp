from django.contrib import admin

from todo.models import Course

# Register your models here. -> add to admin dashboard
#admin.site.register(Product)
class CourseAdmin(admin.ModelAdmin):
    list_display=["id","cname","creator","cprice"]
    list_per_page=8
    
admin.site.register(Course,CourseAdmin)