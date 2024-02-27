key = input('Enter your password: ')
digits = ('1','2','3','4','5','6','7','8','9','0')

def password(key):
   its_valid = True
   if len(key) < 8  :
    print('The password is too short')
    its_valid = False
   elif len(key) > 20 :
    print('The password is too long')
    its_valid = False
   has_digits = False
   for line in key :
    if line in digits :
     has_digits = True
     break
   if has_digits == False :
    print('The password does not contain a digit')
    its_valid = False
   if len(key) != len(set(key)) :
    print('The password contains duplicate characters')
    its_valid = False
   if its_valid == True :
    print('valid password')
   else :
    print('invalid password')
password(key)
