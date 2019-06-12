def allowed_drinks(myage):
    drink_age = myage/2 + 7
    return  drink_age

a = input()
b = allowed_drinks(int(a))


print('I can drink alcohol at the age of '+ str(b) + 'or older')