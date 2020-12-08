import json
from pprint import pprint

data = {'title': 'weelcom',
        'username': 'ALex',
        'goods': [
            {'name': 'Джинсы', 'price': 568},
            {'name': 'Толстовка', 'price': 1500},
        ],
        # 'promotion': True,
        'promotion_prods': [
            {'name': 'Туфли', 'price': 2100}
        ],
        }

with open('m_cadrs.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=4)

with open('m_cadrs.json', 'r', encoding='utf-8') as f:
    cards = json.load(f)
# #
for el in cards:
    print(el)
print(data['goods'])
for qwe in data['goods']:
    print(qwe['name'], qwe['price'])
