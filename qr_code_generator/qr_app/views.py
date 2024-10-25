# qr_app/views.py

import qrcode
from django.shortcuts import render
from .forms import QRCodeForm

def generate_qr(request):
    qr_code_img = None  
    if request.method == 'POST':
        form = QRCodeForm(request.POST)
        if form.is_valid():
            link = form.cleaned_data['link']
            # Generate the QR code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(link)
            qr.make(fit=True)
            img = qr.make_image(fill_color='green', back_color='black')
            
            from io import BytesIO
            import base64

            buffer = BytesIO()
            img.save(buffer)
            buffer.seek(0)
            qr_code_img = base64.b64encode(buffer.getvalue()).decode()  

    else:
        form = QRCodeForm()

    return render(request, 'generate_qr.html', {'form': form, 'qr_code_img': qr_code_img})
