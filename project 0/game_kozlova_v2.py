"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

number = np.random.randint(1, 101) # загадываем число

def random_predict (number: int = 1) -> int:
    """

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    
    count = 0
    predict_number = 50 # начальное значение
    
    if number == predict_number:
        return count    
    elif number > predict_number:
        
        count += 1
        predict_number += 25  # 50+25
                        
        if number == predict_number:
            return count
        elif number > predict_number:
            count += 1
            predict_number += 12 # 75+12
                        
            if number == predict_number:
                return count
            elif number > predict_number:
                count += 1
                predict_number += 6 # 87+6
                                
                if number == predict_number:
                    return count
                elif number > predict_number:
                    
                    while not (number == predict_number):
                        count += 1
                        predict_number += 1 # 93+1+1+1+1+1+1+1
                    return count
                
                else:
                    
                    while not (number == predict_number):
                        count += 1
                        predict_number -= 1 # 93-1-1-1-1-1-1
                    return count
                          
            else:
                count += 1
                predict_number -= 6 # 87-6
                
                if number == predict_number:
                    return count
                elif number > predict_number:
                    
                    while not (number == predict_number):
                        count += 1
                        predict_number += 1 # 81+1+1+1+1+1
                    return count
                
                else:
                    
                    while not (number == predict_number):
                        count += 1
                        predict_number -= 1 # 81-1-1-1-1-1
                    return count              
                  
        else:
            count += 1
            predict_number -= 12 # 75-12
            
            if number == predict_number:
                return count
            elif number > predict_number:
                count += 1
                predict_number += 6 # 63+6
                
                if number == predict_number:
                    return count
                elif number > predict_number:
                    
                    while not (number == predict_number):
                        count += 1
                        predict_number += 1 # 69+1+1+1+1+1
                    return count
                
                else:
                    
                    while not (number == predict_number):
                        count += 1
                        predict_number -= 1 # 69-1-1-1-1-1
                    return count
                
            else:
                count += 1
                predict_number -= 6 # 63-6
                
                if number == predict_number:
                    return count
                elif number > predict_number:
                    
                    while not (number == predict_number):
                        count += 1
                        predict_number += 1 # 57+1+1+1+1+1
                    return count
                
                else:
                    
                    while not (number == predict_number):
                        count += 1
                        predict_number -= 1 # 57-1-1-1-1-1
                    return count
                      
    else:
        count += 1
        predict_number -= 25 # 50-25
        
        if number == predict_number:
            return count
        elif number > predict_number:
            count += 1
            predict_number += 12 # 25+12
            
            if number == predict_number:
                return count
            elif number > predict_number:
                count += 1
                predict_number += 6 # 37+6
                
                if number == predict_number:
                    return count
                elif number > predict_number:
                    
                    while not (number == predict_number):
                        count += 1
                        predict_number += 1 # 43+1+1+1+1+1
                    return count
                
                else:
                    
                    while not (number == predict_number):
                        count += 1
                        predict_number -= 1 # 43-1-1-1-1-1
                    return count
                
            else:
                count += 1
                predict_number -= 6 # 37-6
                 
                
                if number == predict_number:
                    return count
                elif number > predict_number:
                    
                    while not (number == predict_number):
                        count += 1
                        predict_number += 1 # 31+1+1+1+1+1
                    return count
                
                else:
                    
                    while not (number == predict_number):
                        count += 1
                        predict_number -= 1 # 31-1-1-1-1-1
                    return count
                    
        else:
            count += 1
            predict_number -= 12 # 25-12
            
            if number == predict_number:
                return count
            elif number > predict_number:
                count += 1
                predict_number += 6 # 13+6
                
                if number == predict_number:
                    return count
                elif number > predict_number:
                    
                    while not (number == predict_number):
                        count += 1
                        predict_number += 1 # 19+1+1+1+1+1
                    return count
                
                else:
                    
                    while not (number == predict_number):
                        count += 1
                        predict_number -= 1 # 19-1-1-1-1-1
                    return count
                
            else:
                count += 1
                predict_number -= 6 # 13-6
                 
                if number == predict_number:
                    return count
                elif number > predict_number:
                    
                    while not (number == predict_number):
                        count += 1
                        predict_number += 1 # 7+1+1+1+1+1
                    return count
                
                else:
                    
                    while not (number == predict_number):
                        count += 1
                        predict_number -= 1 # 7-1-1-1-1-1-1
                    return count



def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
    
    
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    print()
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
    