from django.contrib import admin
from .models import Task

@admin.action(description='Добавить в избранные задачи')
def make_favorite(modeladmin, request, queryset):
    queryset.update(is_favorite=True)


@admin.action(description='Отметить как выполненные')
def make_completed(modeladmin, request, queryset):
    queryset.update(is_completed=True)
    
    
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_favorite', 'is_completed')
    actions = [make_completed, make_favorite]
    readonly_fields=('is_completed','is_favorite')
    list_filter = ('is_favorite','is_completed')
    search_fields = ('name', 'description')
