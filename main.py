def outer(x):
    def inner(y):
        return x + y
    return inner

f = outer(5)
print(f(10))  # Chiqaradi: 15

def outer_with_default(x, default=0):
    def inner(y):
        return x + y + default
    return inner

f = outer_with_default(5)
print(f(10))  # Chiqaradi: 15
print(f(0))   # Chiqaradi: 15

def outer_with_default_and_scope(x, default=0):
    def inner(y):
        nonlocal x  # Inner funksiyada outer funksiyadagi x ni o'zgartirish mumkin
        x += 1
        return x + y + default
    return inner

f = outer_with_default_and_scope(5)
print(f(10))  # Chiqaradi: 17
print(f(0))   # Chiqaradi: 18
```

```python
def outer():
    x = 5
    def inner():
        nonlocal x  # Inner funksiyada outer funksiyadagi x ni o'zgartirish mumkin
        x += 1
        return x
    return inner

f = outer()
print(f())  # Chiqaradi: 6
print(f())  # Chiqaradi: 7
print(f())  # Chiqaradi: 8
