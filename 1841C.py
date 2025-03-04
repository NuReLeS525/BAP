# Значения мирских цифр
values = {'A': 1, 'B': 10, 'C': 100, 'D': 1000, 'E': 10000}

# Функция для вычисления стоимости мирского числа
def calculate_value(s):
    total = 0
    max_right = 0  # Максимальное значение справа
    for ch in reversed(s):
        if values[ch] < max_right:
            total -= values[ch]
        else:
            total += values[ch]
            max_right = values[ch]
    return total

# Основная функция
def maximize_mir_number(s):
    # Вычисляем первоначальное значение
    current_value = calculate_value(s)
    max_value = current_value
    
    # Пробуем изменить каждый символ на другой
    for i in range(len(s)):
        original_char = s[i]
        for new_char in 'ABCDE':
            if new_char == original_char:
                continue
            # Создаем новую строку с заменой символа
            new_s = s[:i] + new_char + s[i+1:]
            new_value = calculate_value(new_s)
            max_value = max(max_value, new_value)
    
    return max_value

# Чтение входных данных
t = int(input().strip())
test_cases = []

# Считываем все тесты
for _ in range(t):
    s = input().strip()
    test_cases.append(s)

# Для каждого теста выводим результат
results = [str(maximize_mir_number(s)) for s in test_cases]
print("\n".join(results))
