import numpy as np

number = np.random.randint(1, 101) # загадываем число
print ('number =', number)

# Перебор по интервалам. Каждый в 2 раза меньше предыдущего
    
def random_predict (number):
    predict_number = 50
    
    if number == predict_number:
        return predict_number    
    elif number > predict_number:
        predict_number +=25
                
        if number == predict_number:
            return predict_number
        elif number > predict_number:
            predict_number +=12
                        
            if number == predict_number:
                return predict_number
            elif number > predict_number:
                predict_number +=6
                                
                if number == predict_number:
                    return predict_number
                elif number > predict_number:
                    while not (number == predict_number):
                        predict_number +=1
                    return predict_number
                else:
                    while not (number == predict_number):
                        predict_number -=1
                    return predict_number
                        
                
            else:
                predict_number -=6
                
                if number == predict_number:
                    return predict_number
                elif number > predict_number:
                    while not (number == predict_number):
                        predict_number +=1
                    return predict_number
                else:
                    while not (number == predict_number):
                        predict_number -=1
                    return predict_number
                
                
        else:
            predict_number -=12
            
            if number == predict_number:
                return predict_number
            elif number > predict_number:
                predict_number +=6
                
                if number == predict_number:
                    return predict_number
                elif number > predict_number:
                    while not (number == predict_number):
                        predict_number +=1
                    return predict_number
                else:
                    while not (number == predict_number):
                        predict_number -=1
                    return predict_number
                
            else:
                predict_number -=6
                
                if number == predict_number:
                    return predict_number
                elif number > predict_number:
                    while not (number == predict_number):
                        predict_number +=1
                    return predict_number
                else:
                    while not (number == predict_number):
                        predict_number -=1
                    return predict_number
                
            
    else:
        predict_number -=25
        
        if number == predict_number:
            return predict_number
        elif number > predict_number:
            predict_number +=12
            
            if number == predict_number:
                return predict_number
            elif number > predict_number:
                predict_number +=6
                
                if number == predict_number:
                    return predict_number
                elif number > predict_number:
                    while not (number == predict_number):
                        predict_number +=1
                    return predict_number
                else:
                    while not (number == predict_number):
                        predict_number -=1
                    return predict_number
                
            else:
                predict_number -=6
                 
                
                if number == predict_number:
                    return predict_number
                elif number > predict_number:
                    while not (number == predict_number):
                        predict_number +=1
                    return predict_number
                else:
                    while not (number == predict_number):
                        predict_number -=1
                    return predict_number
                
        else:
            predict_number -=12
            
            if number == predict_number:
                return predict_number
            elif number > predict_number:
                predict_number +=6
                
                if number == predict_number:
                    return predict_number
                elif number > predict_number:
                    while not (number == predict_number):
                        predict_number +=1
                    return predict_number
                else:
                    while not (number == predict_number):
                        predict_number -=1
                    return predict_number
                
            else:
                predict_number -=6
                 
                if number == predict_number:
                    return predict_number
                elif number > predict_number:
                    while not (number == predict_number):
                        predict_number +=1
                    return predict_number
                else:
                    while not (number == predict_number):
                        predict_number -=1
                    return predict_number

print (random_predict(number))
print()