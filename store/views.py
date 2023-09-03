from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ThongTinDonwHangForm
from datetime import datetime, timedelta
from .models import ThongTinDatHang


def index(request):
    user_ip = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    # gui_tu_url = request.META['HTTP_REFERER']

    if request.method == "POST":
        form = ThongTinDonwHangForm(request.POST)
        if form.is_valid():
            now = datetime.now().timestamp()  # Convert `now` to a timestamp
            reset_time = request.session.get('reset_time', now)
            if now >= reset_time:
                request.session['submissions'] = 0
                request.session['reset_time'] = (
                    datetime.now() + timedelta(hours=1)).timestamp()
            submissions = request.session.get('submissions', 0)
            if submissions >= 3:
                form.add_error(None, 'You have exceeded the submission limit.')
            else:
                request.session['submissions'] = submissions + 1
                thongTinDatHang = ThongTinDatHang()
                thongTinDatHang.ten = form.cleaned_data['ten']
                thongTinDatHang.so_dien_thoai = form.cleaned_data['so_dien_thoai']
                thongTinDatHang.dia_chi = form.cleaned_data['dia_chi']
                thongTinDatHang.ip = user_ip
                thongTinDatHang.user_agent = user_agent
                thongTinDatHang.ten_san_pham = form.cleaned_data['san_pham']
                matching_entries = ThongTinDatHang.objects.filter(ip=user_ip)
                if matching_entries.count() >= 10:
                    matching_entries.update(du_doan='SPAM')
                    thongTinDatHang.du_doan = 'SPAM'

                thongTinDatHang.save()

        else:
            form = ThongTinDonwHangForm(request.POST)

    else:
        form = ThongTinDonwHangForm()

    return render(request, 'fraud-protection-form.html', {"form": form})
