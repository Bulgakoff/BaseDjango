import json
from pprint import pprint

cards = [
    {'categ': 'Одежда',
     'goods': [{
         'name': 'Худи черного цвета с '
                 'монограммами adidas Originals',
         'price': 6090.00,
         'description': 'Мягкая ткань для свитшотов.'
                        ' Стиль и комфорт – это образ жизни.',
         'quantity': 51,
         'image': '/static/vendor/img/products/qwe1.jpg'
     }, {
         'name': 'Синяя куртка The North Face',
         'price': 23725.00,
         'description': 'Гладкая ткань.'
                        ' Водонепроницаемое покрытие.'
                        ' Легкий и теплый пуховый наполнитель.',
         'quantity': 12,
         'image': '/static/vendor/img/products/qwe2.jpg'
     }, {
         'name': 'Коричневый спортивный '
                 'oversized-топ ASOS DESIGN',
         'price': 3390.00,
         'description': 'Материал с плюшевой текстурой.'
                        ' Удобный и мягкий.',
         'quantity': 10,
         'image': '/static/vendor/img/products/qwe4.jpg'
     }, {
         'name': 'Темно-синие широкие '
                 'строгие брюки ASOS DESIGN',
         'price': 2890.00,
         'description': 'Легкая эластичная ткань'
                        ' сирсакер Фактурная ткань.',
         'quantity': 35,
         'image': '/static/vendor/img/products/qwe3.jpg'
     }]
     },
    {'categ': 'Рюкзаки',
     'goods': [{
         'name': 'Пестрый рюкзак'
                 ' Nike Heritage',
         'price': 2340.00,
         'description': 'Плотная ткань.'
                        ' Легкий материал.',
         'quantity': 11,
         'image': '/static/vendor/img/products/rukzak.jpg'
     }, {
         'name': 'Рюкзак WENGER NARROW HIKING PACK 13022215 черный',
         'price': 4540.00,
         'description': 'Кожа',
         'quantity': 131,
         'image': '/static/vendor/img/products/rukzak2.jpg'
     }]
     },
    {'categ': 'Обувь',
     'goods': [{
         'name': 'Коричневые Кроссовки на платформе с'
                 ' 3 парами люверсов Dr Martens 1461 Bex',
         'price': 13590.00,
         'description': 'Гладкий кожаный верх.'
                        ' Натуральный материал.',
         'quantity': 8,
         'image': '/static/vendor/img/products/tuthli.jpg'
     }, {
         'name': 'Ralf Ringer',
         'price': 1590.00,
         'description': 'Материал верха: натуральная кожа Внутренний материал:'
                        ' шерстяной мех.Материал подошвы:'
                        ' термопластиковая резина',
         'quantity': 85,
         'image': '/static/vendor/img/products/bott.jpg'
     }]
     }
]

with open('cloth_cadrs.json', 'w') as f:
    json.dump(cards, f, indent=4)

with open('cloth_cadrs.json', 'r', encoding='utf-8') as f:
    cards = json.load(f)

for card in cards:
    # print(card['categ'])
    # print(card['goods'])
    print(card['goods'][0]['name'])
    print(card['goods'][0]['price'])
    print(card['goods'][0]['description'])
    print(card['goods'][0]['quantity'])
    print(card['goods'][1]['image'])
    print('================================')
