from django.contrib import admin
from django.utils.safestring import mark_safe

from course.models import Category, Course, Lesson, Tag
# Register your models here.

class MyLessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'Active', 'Created_date']
    search_fields = ['subject']
    list_filter = ['id', 'Created_date']
    list_editable = ['subject']
    readonly_fields =  ['image_view']

    def image_view(self, lesson):
        return mark_safe(f"<img src='/static/{lesson.image.name}' width=200/>")

    class Media:
        css = {
            'all': ('/static/css/styles.css', )
        }


admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson, MyLessonAdmin)
admin.site.register(Tag)
