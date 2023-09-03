from django import forms
from django.core.validators import RegexValidator


class ThongTinDonwHangForm(forms.Form):
    ten = forms.CharField(error_messages={
        'required': 'Vui lòng nhập họ và tên',
    },
        widget=forms.TextInput(attrs={
            'placeholder': 'Họ và tên',
        })
    )
    so_dien_thoai = forms.CharField(error_messages={
        'required': 'Vui lòng nhập số điện thoại',
    },
        validators=[
        RegexValidator(
            regex=r'^(03|05|07|08|09|01[2|6|8|9])+([0-9]{8})\b',
            message="Số điện thoại không hợp lệ."
        )
    ],
        widget=forms.TextInput(attrs={
            "placeholder": "Số điện thoại"
        })
    )
    dia_chi = forms.CharField(error_messages={
        'required': 'Vui lòng nhập địa chỉ',
    },
        widget=forms.TextInput(attrs={
            "placeholder": "Địa chỉ"
        })
    )
    san_pham = forms.CharField(error_messages={
        'required': 'Vui lòng nhập tên sản phẩm',
    },
        widget=forms.TextInput(attrs={
            "placeholder": "Tên sản phẩm"
        })
    )
