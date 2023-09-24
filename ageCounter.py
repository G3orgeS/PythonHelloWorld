name = input('Vad är ditt namn?')

print(f'Hej, {name}')

birthdate = input('När är du född (åååå-mm-dd)?')

from datetime import datetime
birthdate = datetime.strptime(birthdate, '%Y-%m-%d').year
currantYear = datetime.now().year
age = currantYear - birthdate

print(f'Du är ca {age} år')