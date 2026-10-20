# ماشین حساب ساده

این پروژه چهار عمل اصلی ماشین حساب را فراهم می‌کند:

- جمع: `add(a, b)`
- تفریق: `subtract(a, b)`
- ضرب: `multiply(a, b)`
- تقسیم: `divide(a, b)`

در صورت تقسیم بر صفر، تابع `divide` خطای `ValueError` ایجاد می‌کند.

## نمونه استفاده

```python
from calculator import add, subtract, multiply, divide

print(add(2, 3))        # 5
print(subtract(7, 4))   # 3
print(multiply(6, 5))   # 30
print(divide(8, 2))     # 4.0
```

## اجرای تست‌ها

```bash
python3 -m unittest -v test_calculator.py
```
