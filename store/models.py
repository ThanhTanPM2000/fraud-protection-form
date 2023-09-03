from django.db import models

# Create your models here.


class ThongTinDatHang(models.Model):
    DU_DOAN_THONG_TIN = [
        ('SPAM', 'Người dùng Spam'),
        ("ACTUAL", "Người dùng thực tế")
    ]
    ten = models.CharField(max_length=100)
    so_dien_thoai = models.CharField(max_length=20)
    dia_chi = models.CharField(max_length=200)
    du_doan = models.CharField(
        max_length=10, choices=DU_DOAN_THONG_TIN, default="ACTUAL")
    ip = models.CharField(max_length=20, blank=True, null=True)
    user_agent = models.CharField(max_length=200, blank=True, null=True)
    gui_tu_url = models.CharField(max_length=200, blank=True, null=True)
    thoi_gian_gui = models.DateTimeField(auto_now_add=True)
    ten_san_pham = models.CharField(max_length=100, )

    def __str__(self):
        return self.ten + " - " + self.so_dien_thoai

    class Meta:
        ordering = ['-thoi_gian_gui']
        indexes = [models.Index(fields=['ten', "so_dien_thoai"])]


# class SanPham(models.Model):
#     ten = models.CharField(max_length=100)
#     gia = models.IntegerField()
#     so_luong = models.IntegerField()


# class KhuyenMai(models.Model):
#     ten = models.CharField(max_length=100)
#     gia_tri = models.IntegerField()
#     so_luong = models.IntegerField()


# class SanPhamKhuyenMai(models.Model):
#     san_pham = models.ForeignKey('SanPham', on_delete=models.PROTECT)
#     khuyen_mai = models.ForeignKey('KhuyenMai', on_delete=models.PROTECT)
#     gia = models.IntegerField()
#     so_luong = models.IntegerField()
