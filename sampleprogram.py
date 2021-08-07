''' patient = 'John Smith'
age = 20
is_patient_new = True '''

''' name = input('What is your name? ')
color = input('What is your fav color? ')
print(name +' likes '+ color )  '''

''' birth_year = input('Birth Year: ')
age = 2020 - int(birth_year)
print(age)  '''

''' weight_pounds = int(input('Weight(pounds): '))
weight_kg = weight_pounds * 0.45
print(weight_kg)   '''

'''  course = 'Python for Beginners'
print(course[-9:-2])
print(course[11:18])
print(course[1:-1])   '''

'''  first, last = 'Prem', 'Sankar'
msg = f'{first} [{last}] got a new job in python'
print(msg)  '''

'''  course = 'Python for Beginners'
print(course.find('Beginners'))
print(course.replace('Beginner','Absolute Beginners'))
print(course.count('n'))
print('python' in course)
print(course.title())  '''

''' is_hot = False
is_cold = False
if is_hot:
    print('Its a hot day Drink Plenty of Water')
elif is_cold:
    print('its a cold day Wear warm Clothes')
else:
    print('Its a Lovely day')   '''

'''  price = 1000000
is_buyer_good = True
if is_buyer_good:
    down_payment = (price*10)/100
    final_price = price - down_payment
    print(final_price)
else:
    down_payment = (price*20)/100
    final_price = price - down_payment
    print(final_price)   '''

'''   name = len(input('Enter name: '))
if name < 3:
    print('length is not enough')
elif name > 50:
    print('length is more')
else:
    print('length is good')   '''

# Program to find Weight conversion from Kg to Lbs and vice versa:

'''   weight = int(input('Enter weight: '))
weight_in = input('L(lbs) or K(kg): ')
if weight_in.upper() == 'L':
    calc_weight = weight * 0.45
    print(f'You are {calc_weight} kilos ')
else:
    calc_weight = weight / 0.45
    print(f'You are {calc_weight} pounds')   '''

# Guessing Game:

''' secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input('Enter secret number: '))
    guess_count += 1
    if guess == secret_number:
        print('You win')
        break
else:
    print('you failed')    '''

# Car Game:

# help - to get the list of commands to do
# 1 start - start the car
# 2 stop - stop the car
# 3 quit - quit the game

''' is_car_started = ''
while True:
    command = input('> ').lower()
    if command == 'start':
        if is_car_started:
            print('Car already started')
        else:
            is_car_started = True
            print('Start the car')
    elif command == 'stop':
        if not is_car_started:
            print('Car already stopped')
        else:
            is_car_started = False
            print('Stop the car')
    elif command == 'help':
        print('Start - to start the car\nStop - to stop the car\nquit - to exit the game')
    elif command == 'quit' or 'exit':
        break
    else:
        print('I do not understand that')    '''


'''   
prices = [10,20,30,40,50]
total = 0
for cost in prices:
    total += cost
print(total)   '''


'''   numbers = [5, 4, 3, 2, 1]
for i in numbers:
    output = ''
    for j in range(i):
        output += 'x'
    print(output)   '''

'''  numbers = [12, 99, 45, 34, 67]
max = numbers[0]
for i in numbers:
    if i > max:
        max = i
print(max)    '''

'''
numbers = [23, 4, 5, 1, 23, 5, 90, 9]
unique_no = []
for number in numbers:
    if number not in unique_no:
        unique_no.append(number)
        unique_no.sort()
print(unique_no)  '''


#Phone number from numbers to words:
'''
ph = input('phone: ')
dicti = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five',
        '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '0': 'zero'}
output = ''
for ch in ph:
    output += dicti[ch] + ' '
print(output)    '''

#Phone number from words to numbers:  need to check this *********************************************************
'''
ph = input('phone in strings: ')
dicti = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
        'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'zero': 0}
output = 0
for ch in ph:
    output += dicti[ch]
print(output)       '''


# Emoji Converter:
'''
char = input('> ')
words = char.split(' ')
print(words)
emoji = {':)': '😊', ':(': '😟'}
output = ' '
for word in words:
    output += emoji.get(word, word) + ' '
print(output)     '''

#fibonacci series:

a, b = 0, 1







