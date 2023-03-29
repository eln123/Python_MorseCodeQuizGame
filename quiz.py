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


def filterLenFunc(dict_filter):
    filtered_dict = {}
    for char in morseCodeDict:
      length = len(morseCodeDict[char])
      if length == dict_filter:
        filtered_dict[char] = morseCodeDict[char]
    return filtered_dict

def generate_new__numbers_letters(dict, letter, count):
    returnDict = {}
    for num in dict:
        if dict[num] != letter:
            count = str(count)
            returnDict[count] = dict[num]
            count = int(count)
            count += 1
    
    return returnDict

def main():

    while True:
        filter = input("Do you want to be quizzed for 1, 2, 3, 4 character codes, or all? (Type '1', '2', '3', '4', or 'No filter') ")
        if filter.isdigit():
            number = int(filter)
            morseCodeDict = filterLenFunc(number)
            break
        elif filter == 'No filter':
            break
        else:
            print("Invalid")
            continue

     # for loop through morseCodeList, to generate dict of numbers and remaining letters to generate random letter from
    
    numbers_letters = {}
    count = 0

    for letter in morseCodeDict:
            numbers_letters[str(count)] = letter
            count += 1

    print("What is the Morse code for...")

   
    while True:
        # generate random letter for next question
        len_of_numbers_letters = len(numbers_letters)
        randomNumber = random.randint(0,  len_of_numbers_letters - 1)
        randomLetter = numbers_letters[str(randomNumber)]
        print(randomLetter)

        # ask question with while loop (keeps asking the question until you are correct)
        correct = False

        while correct == False:
            answer = input(str(randomLetter) + ": ")

             # if you are correct, filter the dictionary to get the letter out, then break out of while loop for this question
            if str(answer) == morseCodeDict[randomLetter]: 
                 print('correct!')
                 count = 0
                 numbers_letters = generate_new__numbers_letters(numbers_letters, randomLetter, count)
                 break
            
            # else print("Incorrect") and continue to next iteration of question
            else:
                print("Incorrect")

        # if no more remaining letters: stop, else: continue to next random generated letter
        if len(numbers_letters) == 0:
            print("Great job. Here's your empty numbers_letters: ", numbers_letters)
            print("That's all of them!")
            break
        else: 
            continue

       
       

main()