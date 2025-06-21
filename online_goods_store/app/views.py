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

def order_placing(request):
    return render(request, 'order_placing.html')

def authorization(request):
    user=Customer.objects.all()
    if 'login' in request.POST:
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        if user.filter(phone=phone).exists() and user.filter(password=password).exists():
            return HttpResponseRedirect (reverse ('personal_account'), {'customerid': user.get(phone=phone).customerid})
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
        font_path = os.path.join('C:/Users/Compolis/OneDrive/Рабочий стол/Интернет магазин для продажа товаров(полы)/ВЕБ РАЗРАБОТКА/Web_Online_Goods_Store/online_goods_store/app/static/fonts', 'arial.ttf')
        pdfmetrics.registerFont(TTFont('Arial', font_path))

        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='RussianArial', fontName='Arial', fontSize=10, leading=12))

        title = Paragraph("Отчет по товарам и категориям", styles['RussianArial'])

        # Данные в формате:
        # Категория -> список товаров
        # Товар -> список характеристик (каждая характеристика — словарь)
        data_dict = {
            'Основной товар': [
                {
                    'name': 'Инженерная доска Lab Arte от 400 до 1500х145х14/2,5 Дуб Натур Кайт Лак*',
                    'details': [
                        {'status': 'Под заказ', 'unit': 'м²', 'price': '5 377,00', 'available_now': '', 'available_order': '353,007'},
                    ]
                },
                {
                    'name': 'Инженерная доска Lab Arte от 400 до 1500х145х14/2,5 Дуб Натур Табак Лак*',
                    'details': [
                        {'status': 'В наличии', 'unit': 'м²', 'price': '5 377,00', 'available_now': '', 'available_order': '366,510'},
                    ]
                },
                # Добавьте остальные товары...
            ],
            'LabArte Техномассив Royal Parket': [
                {
                    'name': 'Инженерная доска 14мм',
                    'details': [
                        {'status': 'В наличии', 'unit': 'м²', 'price': '2,310', 'available_now': '1 921,845', 'available_order': '-198,660'},
                    ]
                },
                # ...
            ],
            # Другие категории...
        }

        # Формируем данные таблицы
        # Заголовок таблицы
        data = [
            [
                Paragraph('<b>Категория</b>', styles['RussianArial']),
                Paragraph('<b>Название товара</b>', styles['RussianArial']),
                Paragraph('<b>Статус товара</b>', styles['RussianArial']),
                Paragraph('<b>Ед.изм</b>', styles['RussianArial']),
                Paragraph('<b>Розничная цена</b>', styles['RussianArial']),
                Paragraph('<b>Доступно сейчас</b>', styles['RussianArial']),
                Paragraph('<b>Доступно под заказ</b>', styles['RussianArial']),
            ]
        ]

        # Заполняем строки с объединениями ячеек для категорий
        for category, products in data_dict.items():
            # Считаем сколько строк займет категория (сумма всех характеристик всех товаров)
            category_row_count = sum(len(p['details']) for p in products)

            first_cat_row = len(data)  # индекс первой строки категории в data

            for product in products:
                details = product['details']
                first_prod_row = len(data)
                for i, d in enumerate(details):
                    row = []
                    # Категория - только для первой строки товара и первой характеристики категории
                    if i == 0 and first_prod_row == first_cat_row:
                        # Категория будет объединена на category_row_count строк
                        row.append(Paragraph(category, styles['RussianArial']))
                    elif i == 0:
                        # Для первой строки товара, но не первой категории - пусто, объединено ниже
                        row.append('')
                    else:
                        # Для остальных строк товара - пусто
                        row.append('')

                    # Название товара - только для первой характеристики товара
                    if i == 0:
                        row.append(Paragraph(product['name'], styles['RussianArial']))
                    else:
                        row.append('')

                    # Остальные поля
                    row.append(Paragraph(d.get('status', ''), styles['RussianArial']))
                    row.append(Paragraph(d.get('unit', ''), styles['RussianArial']))
                    row.append(Paragraph(d.get('price', ''), styles['RussianArial']))
                    row.append(Paragraph(d.get('available_now', ''), styles['RussianArial']))
                    row.append(Paragraph(d.get('available_order', ''), styles['RussianArial']))

                    data.append(row)

            # Добавим объединения ячеек для категории
            data_len = len(data)
            data_rows_for_category = data_len - first_cat_row
            # Объединяем ячейку категории по вертикали
            if data_rows_for_category > 1:
                # (col, row_start) до (col, row_end)
                # Категория в колонке 0
                data.append([''])  # чтобы не выйти за границы, потом удалим
                # Добавим стиль объединения ниже

        # Создаем таблицу
        col_widths = [90, 100, 80, 40, 80, 80, 80]

        table = Table(data, colWidths=col_widths)

        # Создаем стиль таблицы
        style = TableStyle([
            ('FONTNAME', (0, 0), (-1, -1), 'Arial'),
            ('FONTSIZE', (0, 0), (-1, -1), 9),
            ('ALIGN', (2, 0), (-1, -1), 'CENTER'),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
            ('GRID', (0,0), (-1,-1), 0.5, colors.grey),
            ('BACKGROUND', (0,0), (-1,0), colors.lightgrey),
        ])

        # Добавим объединения ячеек для категорий и товаров
        row_idx = 1  # начинаем со строки после заголовка
        for category, products in data_dict.items():
            cat_row_count = sum(len(p['details']) for p in products)
            # Объединяем категорию по вертикали
            if cat_row_count > 1:
                style.add('SPAN', (0, row_idx), (0, row_idx + cat_row_count -1))
            # Для каждого товара объединяем название товара по вертикали
            prod_row_idx = row_idx
            for product in products:
                details_count = len(product['details'])
                if details_count > 1:
                    style.add('SPAN', (1, prod_row_idx), (1, prod_row_idx + details_count - 1))
                prod_row_idx += details_count
            row_idx += cat_row_count

        table.setStyle(style)

        # Формируем документ
        buffer = BytesIO()
        doc = SimpleDocTemplate(buffer, pagesize=letter, leftMargin=20, rightMargin=20, topMargin=20, bottomMargin=20)
        elements = [title, Spacer(1, 12), table]
        doc.build(elements)

        pdf = buffer.getvalue()
        buffer.close()

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="report.pdf"'
        response.write(pdf)
        return response
    return render(request, 'reporting.html')

def personal_account(request):
    return render(request, 'personal_account.html')

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
