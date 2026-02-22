def demo_function(required, *args, **kwargs):
    """
    Демонстрирует работу *args и **kwargs.
    required - обязательный аргумент.
    *args - соберет лишние позиционные аргументы в кортеж.
    **kwargs - соберет лишние именованные аргументы в словарь.
    """
    print(f"1. Обязательный аргумент: {required}")

    print(f"2. *args (кортеж позиционных аргументов): {args}")
    for i, arg in enumerate(args):
        print(f"   args[{i}] = {arg}")

    print(f"3. **kwargs (словарь именованных аргументов): {kwargs}")
    for key, value in kwargs.items():
        print(f"   kwargs['{key}'] = {value}")


# Пример вызова функции
print("--- Вызываем функцию ---")
demo_function("обязательное_значение", 100, 200, 300, name="Анна", age=30, city="Москва")