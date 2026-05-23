import json
import re
import random

# 读取JSON数据
with open('E:/qqfile/dishes.json', 'r', encoding='utf-8') as f:
    dishes = json.load(f)

# 类别映射
category_map = {
    '面食': '面食', '粉类': '面食', '面/粉': '面食', '汤面': '面食',
    '饺子': '小吃', '馄饨': '小吃', '云吞': '小吃', '面点': '小吃',
    '汤': '汤类',
    '小荤/素菜': '米饭', '荤菜': '米饭', '大荤': '米饭', '素菜': '米饭',
    '主食': '米饭', '炒饭': '米饭',
    '盖浇饭': '盖浇饭', '铁板饭': '盖浇饭', '木桶饭': '盖浇饭',
    '小火锅': '盖浇饭', '火锅': '汤类',
    '麻辣烫': '面食', '烤盘饭': '盖浇饭', '自助称重': '米饭',
    '套餐': '盖浇饭', '卤味': '小吃', '烧腊饭': '米饭', '煲仔饭': '盖浇饭', '拌饭': '盖浇饭'
}

# 烹饪方式映射
cooking_map = {
    '面食': '煮', '粉类': '煮', '面/粉': '煮', '汤面': '煮',
    '饺子': '蒸', '馄饨': '煮', '云吞': '煮', '面点': '蒸',
    '汤': '煮', '小火锅': '煮', '火锅': '煮',
    '麻辣烫': '煮',
    '自助称重': '炒', '套餐': '烤', '卤味': '卤',
    '烧腊饭': '烤', '煲仔饭': '煮', '拌饭': '炒'
}

# 辣度映射
spicy_map = {
    '清淡': 0, '原味': 0, '清甜': 0, '鲜甜': 0, '清爽': 0,
    '酸甜': 0, '咸鲜': 0, '鲜香': 0, '鲜美': 0, '清鲜': 0,
    '浓郁': 0, '甜咸': 0, '酱香': 0, '药膳味': 0, '油香': 0,
    '可选': 0,
    '微辣': 1, '花生酱味': 1, '孜然': 1, '甜辣': 1,
    '中辣': 2, '酸辣': 2, '香辣': 2,
    '麻辣': 3, '重辣': 3
}

# 健康类型映射
health_map = {
    '素菜': ['vegetarian', 'low_oil'],
    '小荤/素菜': ['balanced'],
    '主食': ['vegetarian'],
    '大荤': ['high_protein'],
    '荤菜': ['high_protein', 'balanced']
}

# 饱腹感映射
satiety_map = {
    '主食': 'heavy', '大荤': 'heavy', '套餐': 'heavy',
    '盖浇饭': 'heavy', '铁板饭': 'heavy', '木桶饭': 'heavy', '煲仔饭': 'heavy', '拌饭': 'heavy',
    '小火锅': 'heavy', '火锅': 'medium',
    '面食': 'medium', '粉类': 'medium', '面/粉': 'medium', '汤面': 'medium',
    '汤': 'light',
    '小荤/素菜': 'medium', '荤菜': 'medium',
    '饺子': 'light', '馄饨': 'light', '云吞': 'light', '面点': 'light',
    '麻辣烫': 'medium',
    '烤盘饭': 'medium', '自助称重': 'medium',
    '烧腊饭': 'medium', '卤味': 'light'
}

def parse_price(price_str):
    """解析价格字符串"""
    # 移除"元/..."等后缀
    match = re.search(r'([\d.]+)', str(price_str))
    if match:
        return float(match.group(1))
    return 0

def convert_dish(dish, index):
    """转换单个菜品"""
    dish_type = dish.get('菜品类型', '')
    flavor = dish.get('菜品口味', '')
    price = parse_price(dish.get('菜品价格', '0'))

    # 基本字段
    item = {
        'id': index + 1,
        'name': dish.get('菜品名称', ''),
        'window': dish.get('窗口位置', ''),
        'category': category_map.get(dish_type, '米饭'),
        'temp': '热',
        'cooking': cooking_map.get(dish_type, '炒'),
        'spicy': spicy_map.get(flavor, 0),
        'price': price,
        'satiety': satiety_map.get(dish_type, 'medium'),
        'health': health_map.get(dish_type, ['balanced']),
        'rating': round(random.uniform(4.0, 4.9), 1),
        'popularity': random.randint(60, 95),
        'isNew': random.random() < 0.1,
        'isHot': random.random() < 0.2,
        'tags': [dish_type, flavor],
        'description': f"{dish.get('窗口位置', '')} - {flavor}口味"
    }
    return item

# 转换所有菜品
food_database = [convert_dish(dish, i) for i, dish in enumerate(dishes)]

# 输出JSON格式
print(json.dumps(food_database, ensure_ascii=False, indent=4))
