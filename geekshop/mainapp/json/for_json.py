import json
from pprint import pprint


data = {'title': 'weelcom',
        'username': 'ALex',
        'goods': [
            {'name': 'Джинсы', 'price': 4500},
            {'name': 'Толстовка', 'price': 1500},
        ],
        # 'promotion': True,
        'promotion_prods': [
            {'name': 'Туфли', 'price': 2100}
        ],
        }

with open('m_cadrs.json', 'w') as f:
    json.dump(data, f, indent=4)

# with open('mus_cadrs.json', 'r', encoding='utf-8') as f:
#     cards = json.load(f)
#
# for el in cards:
#     # print(el['categ'])
#     # print(el['goods'])
#     print(el['goods'][2]['name'])
#     print(el['goods'][2]['cost'])
#     print(el['goods'][2]['description'])
#     print(el['goods'][2]['quantity'])
#     print(el['goods'][2]['image'])
#     print('================================')
