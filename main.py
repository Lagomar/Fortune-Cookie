import random
lucky_number = random.randint(1,100) #Generates a number between values
fortune_number = random.randint(1,3)
fortune_text = ""

if fortune_number == 1: 
    fortune_text = "You will have a great day!"
if fortune_number == 2: 
    fortune_text = "Not so good today! Bring an umbrella!"
else: 
    fortune_text = "I honestly don't know!"

print(f'{fortune_text} Your Lucky Number is: {fortune_number}!')

