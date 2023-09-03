from django.contrib import admin
from . import models


@admin.register(models.ThongTinDatHang)
class ThongTinDatHangAdmin(admin.ModelAdmin):
    actions = ['mark_spam', 'mark_phone_spam',
               'mark_ip_spam', 'mark_phone_actual', 'mark_ip_actual']
    list_display = ('ten', 'so_dien_thoai', 'dia_chi', 'du_doan', 'ip',
                    'user_agent', 'gui_tu_url', 'thoi_gian_gui', 'ten_san_pham')
    list_filter = ('du_doan', 'thoi_gian_gui')
    search_fields = ('ten', 'so_dien_thoai', 'dia_chi', 'ip',
                     'user_agent', 'gui_tu_url', 'ten_san_pham')
    ordering = ('-thoi_gian_gui',)
    # change_list_template = 'change_list_thongtindathang.html'

    def get_row_css(self, obj, index):
        if obj.du_doan == 'SPAM':
            return 'red'
        elif obj.du_doan == 'ACTUAL':
            return 'green'
        else:
            return ''

    @admin.action(description='Đánh dấu tất cả là spam')
    def mark_spam(self, request, queryset):
        queryset.update(du_doan='SPAM')

    @admin.action(description="Đánh dấu tất cả số điện thoại này là spam")
    def mark_phone_spam(self, request, queryset):
        queryset.update(du_doan='SPAM')
        for obj in queryset:
            models.ThongTinDatHang.objects.filter(
                so_dien_thoai=obj.so_dien_thoai).update(du_doan='SPAM')

    @admin.action(description="Đánh dấu tất cả địa chỉ ip này là spam")
    def mark_ip_spam(self, request, queryset):
        queryset.update(du_doan='SPAM')
        for obj in queryset:
            models.ThongTinDatHang.objects.filter(
                ip=obj.ip).update(du_doan='SPAM')

    @admin.action(description="Đánh dấu tất cả số điện thoại này là người dùng thực tế")
    def mark_phone_actual(self, request, queryset):
        queryset.update(du_doan='ACTUAL')
        for obj in queryset:
            models.ThongTinDatHang.objects.filter(
                so_dien_thoai=obj.so_dien_thoai).update(du_doan='ACTUAL')

    @admin.action(description="Đánh dấu tất cả địa chỉ ip này là người dùng thực tế")
    def mark_ip_actual(self, request, queryset):
        queryset.update(du_doan='ACTUAL')
        for obj in queryset:
            models.ThongTinDatHang.objects.filter(
                ip=obj.ip).update(du_doan='ACTUAL')
