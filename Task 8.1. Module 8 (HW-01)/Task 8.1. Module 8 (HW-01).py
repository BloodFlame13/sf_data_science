import numpy as np

def game_core_v3():
    
    """
    Returns:
        count (int): Average number of attempts to guess a number.
    """
    
    def Binary_search_parody(number, left, right, count=0) -> int:
        
        """
        Args:
            number (_type_): The number we are guessing.
            left (_type_): Left border of a series of numbers from 1 to 100
            right (_type_): Right border of a series of numbers from 1 to 100
            count (int, optional): Number of iterations.

        Returns:
            count (int): Number of guessing attempts.
        """
        
        # Определяем серединное значение из числового ряда поиска.
        middle = left + (right - left) // 2
    
        if number < middle:
            right = middle - 1 # Нужно сдвинуть правую границу на 1, чтобы исключить middle из следующего поиска.
            count += 1
            return Binary_search_parody(number, left, right, count)
        elif number > middle:
            left = middle + 1  # Нужно сдвинуть левую границу на 1, чтобы исключить middle из следующего поиска.
            count += 1
            return Binary_search_parody(number, left, right, count)
        else:
            count += 1
            return count
    
    count_ls = []
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел
    
    # Добавляем в список количество попыток угадывания.
    for number in random_array:
        count_ls.append(Binary_search_parody(number, left=1, right=100))
    
    # При помощи встроенного метода mean из библиотеки numpy, находим среднее количество попыток угадывания.
    count = int(np.mean(count_ls))
    
    return count

print(f'Среднее количество попыток отгадывания числа в при 1000 повторений = {game_core_v3()}')