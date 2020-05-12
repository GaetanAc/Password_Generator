import random , string

def password(length,num = False,strength='weak'):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    number = string.digits
    punctuation = string.punctuation
    letters = lower + upper
    pwd = ''
    if strength == 'Faible':
        if num :
            length -= 3
            for y in range(3):
                pwd += random.choice(number)
            for y in range (length):
                pwd += random.choice(lower)
    elif strength == 'Moyen' :
        if num :
            length -= 5
            for y in range(5):
                pwd += random.choice(number)
            for y in range(length):
                pwd += random.choice(letters)
    elif strength == 'Fort' :
        if num :
            length -= 7
            for y in range(7):
                pwd += random.choice(punctuation)
            for y in range(length):
                pwd += random.choice(letters)

    pwd = list(pwd)
    random.shuffle(pwd)
    print(''.join(pwd))



Choix = (input('Choisissez un type de mot de passe parmit les 3 propositions : Faible (8 caractères)  , Moyen(16 caractères) , Fort(32 caractères) :'))
if Choix == 'Faible' :
    password(8, num=True, strength= 'Faible')
elif Choix == 'Moyen':
    password(16,num = True ,strength = 'Moyen')
elif Choix == 'Fort':
    password(32, num=True, strength='Fort')
else :
    print("Faux")



