try:
    age=int(input('enter age '))
    income=20000
    risk=income/age
    print(age)
except ValueError:
    print('enter numeric value')
except ZeroDivisionError:
    print('age cant be zero')
