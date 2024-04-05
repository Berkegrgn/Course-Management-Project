from django.contrib import admin
from .models import Comment, Course,Category, Slider

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title","isActive","isHome","slug","category_list",)
    list_display_links= ("title","slug",)
    prepopulated_fields = {"slug": ("title",),}
    list_filter = ("title","isActive","isHome")
    list_editable = ("isActive","isHome",)
    search_fields = ("title","description")

    def category_list(self, obj):
        html = ""
        for category in obj.categories.all():
            html += category.name + " "
        return html


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name","slug","course_count")
    prepopulated_fields = {"slug": ("name",),}

    def course_count(self,obj):
        return obj.course_set.count()
    
admin.site.register(Slider)

class CommentAdmin(admin.ModelAdmin):
    list_display = ['text', 'rating', 'course','create_at']  # Yorumlar listesinde görüntülenecek alanlar
    list_filter = ['course']  # Yorumlar listesini filtreye alma
    search_fields = ['text']  # Yorumları arama özelliği ekleme

    def has_add_permission(self, request):
        # Yorum ekleme yetkisini devre dışı bırak
        return False

    def has_change_permission(self, request, obj=None):
        # Yorum düzenleme yetkisini devre dışı bırak
        return False

    def delete_selected_comments(self, request, queryset):
        """
        Seçilen yorumları toplu olarak silen özel bir eylem.
        """
        for comment in queryset:
            comment.delete()
        self.message_user(request, "Seçilen yorumlar başarıyla silindi.")

    delete_selected_comments.short_description = "Seçilen yorumları sil"  # Eylemin görünen adını belirtin

admin.site.register(Comment, CommentAdmin)

