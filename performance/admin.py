from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Student, Subject, Marks

class StudentAdmin(BaseUserAdmin):
    model = Student
    list_display = ('username', 'roll_number', 'department')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('roll_number', 'department')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'roll_number', 'department'),
        }),
    )
    search_fields = ('username',)
    ordering = ('username',)

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')

@admin.register(Marks)
class MarksAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'marks_obtained')
    list_filter = ('student', 'subject')

admin.site.register(Student, StudentAdmin)
