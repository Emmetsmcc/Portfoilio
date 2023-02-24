
run ="yes"

while run == "yes":

    morse_dict = {"a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--..", "1": ".----", "2": "..---", "3": "...--","4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.", "0": "-----",
                }

    morse_code_text = str(input("What would you like to convert into morse code?: ").lower())
    morse_code_letters = []
    morse_code = []


    for letter in morse_code_text:
        morse_code_letters.append(letter)


    for code in morse_code_letters:
        if code == " ":
            morse_code.append(" ")
        elif code not in morse_dict :
            print("We can only convert letters and numbers.")
        else :
            morse_code.append(morse_dict[code])

    print(morse_code)

    run = input("Do you wish to continue? Yes or No : ").lower()
    while run not in ("yes", "no"):
        run = input("Please input 'yes' or 'no' : ")
    if run == "no":
        break