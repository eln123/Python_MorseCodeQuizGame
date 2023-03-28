import random

morseCodeDict = {
    'A': '12',
    'B': '2111',
    'C': '2121',
    'D': '211',
    'E': '1',
    'F': '1121',
    'G': '221',
    'H': '1111',
    'I': '11',
    'J': '1222',
    'K': '212',
    'L': '1211',
    'M': '22',
    'N': '21',
    'O': '222',
    'P': '1221',
    'Q': '2212',
    'R': '121',
    'S': '111',
    'T': '2',
    'U': '112',
    'V': '1112',
    'W': '122',
    'X': '2112',
    'Y': '2122',
    'Z': '2211'
}

ALPHABET_LIST = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q','R','S','T','U','V','W','X','Y','Z'
]

def TwoCharacter_FilterFunc(code):
    if code.count() == 2: 
        return True


def main():
    remaining_letters = 26

    characterFilter = input("Do you want to be quizzed for 2, 3, 4 character codes, or all?")
    if characterFilter == '2':
        morseCodeDict_filtered = filter(morseCodeDict, TwoCharacter_FilterFunc) 
        print(morseCodeDict_filtered)

    print("What is the Morse code for...")
   
    while True:
        # while loop through morseCodeList
        randomNumber = random.randint(0, remaining_letters - 1)
        randomLetter = ALPHABET_LIST[randomNumber]
        code = morseCodeDict[randomLetter]
      
        
        correct = False

        while correct == False:
            # while loop that keeps asking the question until you are correct
            answer = input(str(randomLetter) + ": ")
            if str(answer) == code: 
                 print('correct!')
                 ALPHABET_LIST.remove(randomLetter)
                 remaining_letters -= 1
                 correct = True
            else:
                print("Incorrect")

        # if no more remaining letters, stop
        if remaining_letters == 0:
            print("That's all of them!")
            break
       

main()