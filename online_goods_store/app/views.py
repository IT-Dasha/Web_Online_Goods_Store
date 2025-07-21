from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Category, Customer, Order, Purchase, Report
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.conf import settings
import os
from django.core.files.storage import FileSystemStorage

#ГОТОВ
def home(request):
    return render(request, 'home.html')

#ГОТОВ
def catalog(request):
    products = Product.objects.all()
    categoryes = Category.objects.all()
    if request.POST:
        category_id=request.POST.get('categoryid_id')
        search=request.POST.get('search')
        if category_id=='' and search=='':
            products = Product.objects.all()
        elif category_id !='' and search !='':
             products = Product.objects.filter(fk_categoryid=category_id,  price=search)
        elif category_id =='' and search !='':
            products = Product.objects.filter(price=search)
        else:
            products = Product.objects.all()
        products = products.filter(fk_categoryid=category_id) 
        return render(request, 'catalog.html', {'products': products, 'categoryes': categoryes})
    return render(request, 'catalog.html', {'products': products, 'categoryes': categoryes})

#ГОТОВ
def product(request, product_id):
    products = Product.objects.filter(productid=product_id).select_related('fk_categoryid')
    return render(request, 'product.html',context={'products': products})

from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from io import BytesIO
import os

def order_placing(request):
    if 'document' in request.POST:
        font_path = os.path.join('fonts/arial.ttf')
        # Регистрируем шрифт Arial
        pdfmetrics.registerFont(TTFont('Arial', font_path))

        # Создаём HTTP ответ с PDF
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="contract_and_invoice.pdf"'

        # Создаём PDF canvas
        p = canvas.Canvas(response)
        p.setFont('Arial', 12)

        # Заголовок договора
        p.drawString(50, 800, "ДОГОВОР КУПЛИ-ПРОДАЖИ")
        p.setFont('Arial', 10)
        p.drawString(50, 780, "г. Ваш город")
        p.drawString(50, 765, "Дата: ________________")

        # Текст договора
        p.drawString(50, 730, "Заказчик приобрёл товар: Подложка.")
        p.drawString(50, 715, "Доставка осуществляется по адресу: ул. Московская, д. 4.")
        p.drawString(50, 700, "Стороны договорились о следующем:")
        p.drawString(70, 685, "1. Продавец обязуется передать товар, а Заказчик принять и оплатить его.")
        p.drawString(70, 670, "2. Стоимость товара составляет 1000 рублей.")  # Пример цены
        p.drawString(70, 655, "3. Доставка включена в стоимость и будет произведена в срок до 3 дней.")
        p.drawString(50, 640, "Подписи сторон:")
        p.drawString(50, 620, "Продавец: ____________________")
        p.drawString(300, 620, "Заказчик: ____________________")

        # Перейдём на новую страницу для счёта
        p.showPage()
        p.setFont('Arial', 12)
        p.drawString(50, 800, "СЧЁТ НА ОПЛАТУ")
        p.setFont('Arial', 10)
        p.drawString(50, 780, "Покупатель: Заказчик")
        p.drawString(50, 765, "Адрес доставки: ул. Московская, д. 4")

        # Таблица счёта (простой вариант)
        p.drawString(50, 730, "Наименование товара")
        p.drawString(250, 730, "Количество")
        p.drawString(350, 730, "Цена за единицу")
        p.drawString(470, 730, "Сумма")

        p.drawString(50, 710, "Подложка")
        p.drawString(250, 710, "1")
        p.drawString(350, 710, "1000 руб.")
        p.drawString(470, 710, "1000 руб.")

        p.drawString(50, 690, "Доставка")
        p.drawString(250, 690, "1")
        p.drawString(350, 690, "0 руб.")  # Если доставка бесплатна
        p.drawString(470, 690, "0 руб.")

        p.drawString(50, 660, "Итого к оплате:")
        p.drawString(470, 660, "1000 руб.")

        p.drawString(50, 630, "Подпись покупателя: ____________________")

        # Сохраняем PDF
        p.showPage()
        p.save()

        return HttpResponse(response, content_type='application/pdf')
    return render(request, 'order_placing.html')
import os
from django.http import HttpResponse
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from datetime import datetime
def generate_contract_and_invoice(request):
        font_path = os.path.join(
            'C:/Users/Compolis/OneDrive/Рабочий стол/Интернет магазин для продажа товаров(полы)/ВЕБ РАЗРАБОТКА/Web_Online_Goods_Store/online_goods_store/app/static/fonts/arial.ttf'
        )
        pdfmetrics.registerFont(TTFont('Arial', font_path))

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="contract_invoice_receipt.pdf"'

        p = canvas.Canvas(response)
        p.setFont('Arial', 12)

        # Страница 1: Договор
        p.drawString(50, 800, "ДОГОВОР КУПЛИ-ПРОДАЖИ")
        p.setFont('Arial', 10)
        p.drawString(50, 780, "г. Ваш город")
        p.drawString(50, 765, f"Дата: {datetime.now().strftime('%d.%m.%Y')}")
        p.drawString(50, 730, "Заказчик приобрёл товар: Подложка.")
        p.drawString(50, 715, "Доставка осуществляется по адресу: ул. Московская, д. 4.")
        p.drawString(50, 700, "Стороны договорились о следующем:")
        p.drawString(70, 685, "1. Продавец обязуется передать товар, а Заказчик принять и оплатить его.")
        p.drawString(70, 670, "2. Стоимость товара составляет 1000 рублей.")
        p.drawString(70, 655, "3. Доставка включена в стоимость и будет произведена в срок до 3 дней.")
        p.drawString(50, 640, "Подписи сторон:")
        p.drawString(50, 620, "Продавец: ____________________")
        p.drawString(300, 620, "Заказчик: ____________________")

        p.showPage()

        # Страница 2: Счёт на оплату
        p.setFont('Arial', 12)
        p.drawString(50, 800, "СЧЁТ НА ОПЛАТУ")
        p.setFont('Arial', 10)
        p.drawString(50, 780, "Покупатель: Заказчик")
        p.drawString(50, 765, "Адрес доставки: ул. Московская, д. 4")

        # Заголовки таблицы
        p.drawString(50, 730, "Наименование товара")
        p.drawString(250, 730, "Количество")
        p.drawString(350, 730, "Цена за единицу")
        p.drawString(470, 730, "Сумма")

        # Строки товара
        p.drawString(50, 710, "Подложка")
        p.drawString(250, 710, "1")
        p.drawString(350, 710, "1000 руб.")
        p.drawString(470, 710, "1000 руб.")

        p.drawString(50, 690, "Доставка")
        p.drawString(250, 690, "1")
        p.drawString(350, 690, "0 руб.")
        p.drawString(470, 690, "0 руб.")

        p.drawString(50, 660, "Итого к оплате:")
        p.drawString(470, 660, "1000 руб.")

        p.drawString(50, 630, "Подпись покупателя: ____________________")

        p.showPage()

        # Страница 3: Чек оплаты
        p.setFont('Arial', 12)
        p.drawString(50, 800, "ЧЕК ОБ ОПЛАТЕ")
        p.setFont('Arial', 10)
        p.drawString(50, 780, f"Дата оплаты: {datetime.now().strftime('%d.%m.%Y %H:%M')}")
        p.drawString(50, 765, "Покупатель: Заказчик")
        p.drawString(50, 750, "Товар: Подложка")
        p.drawString(50, 735, "Количество: 1")
        p.drawString(50, 720, "Стоимость: 1000 руб.")
        p.drawString(50, 705, "Доставка: 0 руб.")
        p.drawString(50, 690, "Итого оплачено: 1000 руб.")
        p.drawString(50, 660, "Спасибо за покупку!")

        p.showPage()
        p.save()

        return HttpResponse(response, content_type='application/pdf')

def authorization(request):
    user=Customer.objects.all()
    if 'login' in request.POST:
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        if user.filter(phone=phone).exists() and user.filter(password=password).exists():
            return HttpResponseRedirect(reverse('personal_account', args=[user.get(phone=phone).customerid]))
        else:
            return HttpResponseRedirect (reverse ('authorization'))
    return render(request, 'authorization.html')

def registration(request):
    user=Customer.objects.all()
    if 'save' in request.POST:
        firstname = request.POST.get('firstname')
        name = request.POST.get('name')
        middlename = request.POST.get('middlename')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        password = request.POST.get('password')
        if user.filter(firstname=firstname).exists() and user.filter(name=name).exists() and user.filter(middlename=middlename).exists() and user.filter(phone=phone).exists() and user.filter(password=password).exists() and user.filter(address=address).exists():
            return HttpResponse ("Такой пользователь уже существует")
        else:
            new_user = Customer(firstname=firstname, name=name, middlename=middlename, phone=phone, address=address, password=password)
            new_user.save()
        return HttpResponseRedirect (reverse ('authorization'))

    return render(request, 'registration.html')

def output_password(request):
    return render(request, 'output_password.html')

from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from io import BytesIO
import os

def reporting(request):
# Регистрация шрифта Arial с поддержкой кириллицы
        if 'repost' in request.POST:
                            # Путь к файлу шрифта Arial.ttf
            font_path = os.path.join('C:/Users/Compolis/OneDrive/Рабочий стол/Интернет магазин для продажа товаров(полы)/ВЕБ РАЗРАБОТКА/Web_Online_Goods_Store/online_goods_store/app/static/', 'fonts', 'arial.ttf')  # замените на свой путь

            # Регистрируем шрифт Arial
            pdfmetrics.registerFont(TTFont('Arial', font_path))

            # Создаем стиль с шрифтом Arial
            styles = getSampleStyleSheet()
            styles.add(ParagraphStyle(name='RussianArial', fontName='Arial', fontSize=14))

            data = [
                    ['Товар', 'Количество'],
                    ['Плинтус', '10 шт'],
                    ['Подложка', '5 уп.'],
                    ['Ламинат', '20 м²'],
            ]

            buffer = BytesIO()
            doc = SimpleDocTemplate(buffer, pagesize=letter)
            elements = []

            title = Paragraph("Отчет по заказам за февраль", styles['RussianArial'])
            elements.append(title)
            elements.append(Spacer(1, 12))

            # Оборачиваем ячейки таблицы в Paragraph с нужным стилем
            table_data = []
            for row in data:
                row_paragraphs = [Paragraph(cell, styles['RussianArial']) for cell in row]
                table_data.append(row_paragraphs)

            table = Table(table_data, colWidths=[400, 100])

            style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.lightgrey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),

            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),

            ('FONTNAME', (0, 0), (-1, -1), 'Arial'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),  # уменьшили размер шрифта

            ('TOPPADDING', (0, 0), (-1, -1), 12),    # увеличиваем отступ сверху
            ('BOTTOMPADDING', (0, 0), (-1, -1), 12), # увеличиваем отступ снизу

            ('GRID', (0, 0), (-1, -1), 1, colors.black),

            ]) 
            table.setStyle(style)

            elements.append(table)

            doc.build(elements)

            pdf_value = buffer.getvalue()
            buffer.close()

            # Сохраняем PDF на диск (укажите свой путь)
            output_path = os.path.join('C:/Users/Compolis/OneDrive/Рабочий стол/Интернет магазин для продажа товаров(полы)/ВЕБ РАЗРАБОТКА/Web_Online_Goods_Store/online_goods_store', 'test_report.pdf')
            with open(output_path, 'wb') as f:
                f.write(pdf_value)

            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="test_report.pdf"'
            response.write(pdf_value)
            return response
        return render(request, 'reporting.html')

def personal_account(request, customerid):  # было customerid → стало pk
    customer = Customer.objects.get(customerid=customerid)
    return render(request, 'personal_account.html', {'customer': customer})

def change_product(request):
    return render(request, 'personal_account.html')

#ГОТОВ
def add_product(request):
    if 'save' in request.POST:
        product=Product()
        product.productid = request.POST.get("productid")
        product.price = request.POST.get("price")
        product.stockquantity = request.POST.get("stockquantity")
        product.fk_categoryid_id = request.POST.get('categoryid_id')
        product.save()
        id_product=request.POST.get("productid")
        image = request.FILES['image']
        fs = FileSystemStorage()
        # save the image on MEDIA_ROOT folder
        file_name = fs.save(id_product+".png", image)
        # get file url with respect to `MEDIA_URL`
        file_url = fs.url(file_name)
        return HttpResponseRedirect (reverse ('catalog'))
    categoryes = Category.objects.all()
    return render(request, 'change_product.html',{'categoryes': categoryes})


# Create your views here.
