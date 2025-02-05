def task7():
    n = int(input())
    player = True  # True - ход Славы (Stan), False - ход Оли (Ollie)
    p = 1

    while p < n:
        if player:  # Ход Славы
            p *= 9
        else:  # Ход Оли
            p *= 2
        player = not player  # Смена игрока

    return 'Stan wins.' if not player else 'Ollie wins.'

print(task7())
