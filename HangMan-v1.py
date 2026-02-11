# H A N G - M A N:
print("Welcome to the HangMan!")
print(''' ___________.._______''')
print('''| .__________))______|''')
print('''| | / /      ||''')
print('''| |/ /       ||''')
print('''| | /        ||.-\'\'.''')
print('''| |/         |/  _  \\ ''')
print('''| |          ||  `/,|''')
print('''| |          (\\`__.' ''')
print('''| |         .-`--'.''')
print('''| |        /Y . . Y\\ ''')
print('''| |       // |   | \\''')
print('''| |      //  | . |  \\''')
print('''| |     ')   |   |   (`''')
print('''| |          ||'||''')
print('''| |          || ||''')
print('''| |          || ||''')
print('''| |          || ||''')
print('''| |         / | | \\ ''')
print('''""""""""""|_`-' `-' |"""|''')
print('''|"|"""""""\\ \\       '"|"|''')
print('''| |        \\ \\        | |''')
print(''': :         \\ \\       : :  sk''')
print('''. .          `'       . .''')
import random
List = ["apple", "mercedes", "mathmatics", "programming", "python", "trump"]
Random_number = random.randint(0, len(List) - 1)
Target = List[Random_number]        # such as: apple
active = []
Life = 6           # Life == -1 --> means Game over!
for n in range(0, len(Target)):
    active += "_"
stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']

# Set the letters : a _ _ _ _
def Set(letter, Life):
    flag = False
    for n in range(0, len(Target)):
        if letter == Target[n]:
            active[n] = letter
            flag = True
    if flag == True:
        return True
    return False
def Show():
    temp = ""
    for n in range(0, len(Target)):
        temp += active[n]
        temp += "  "
    print(temp + "\n")
def Check_end():
    Temp = ""
    for n in range(0, len(active)):
        Temp += active[n]
    if Temp == Target:
        return True
    return False
def Repeat(letter):
    flag = False
    for n in active:
        if n == letter:
            flag = True
    if flag:
        print(f"You already chose <{letter}>, try something else.")

while Life > 0:
    print(f"Man's Life is: {Life}")
    Show()
    letter = input("Guess a letter to save the man: ").lower()
    from os import system
    system("cls")
    Repeat(letter)
    if Set(letter, Life) == False:
        Life -= 1
        print(f"You chose <{letter}>, that's not in the word, you lose a life.")
    print(stages[6 - Life])
    if Check_end() == True:
        Life = -1
if Life == -1:
    print("Congradulation, You won!")
else:
    print("Sorry, You lost!")