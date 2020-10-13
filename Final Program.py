# Billy Row
# May 24, 2017
# Computer Science I Spring Final

import time
import subprocess

# Countdown for the start of the program
# ======================================================================================================================
xrange = 3
print("The program will start in ", xrange, "second(s).")
time.sleep(1)
while xrange != 1:
    xrange -= 1
    print(xrange, "second(s)")
    time.sleep(1)

# Title
# ======================================================================================================================
print("\033[1;36m,-----.                 ,--.       ,-----.,--.       ,--.                       \033[0m")
print("\033[1;31m|  |) /_  ,---.  ,---.,-'  '-.    '  .--./`--' ,---. |  ,---.  ,---. ,--.--.    \033[0m")
print("\033[1;32m|  .-.  \| .-. :(  .-''-.  .-'    |  |    ,--.| .-. ||  .-.  || .-. :|  .--'    \033[0m")
print("\033[1;33m|  '--' /\   --..-'  `) |  |      '  '--'\|  || '-' '|  | |  |\   --.|  |       \033[0m")
print("\033[1;34m`------'  `----'`----'  `--'       `-----'`--'|  |-' `--' `--' `----'`--'       \033[0m")
print("\033[1;35m                                              `--'                              \033[0m")
subprocess.call(["afplay", "pacman_beginning.wav"])
time.sleep(1)

# Intro/Greeting to the User
# ======================================================================================================================
def intro():
    print("Welcome to the best encryption cipher!\n")
    time.sleep(1.5)
    print("This encryption is more unbreakable than the Enigma Machine!\n")
    time.sleep(1.5)
    user = input("Are you truly ready?\n")

    if user == "yes":
        print("\nAlright. Good luck!")
        time.sleep(1.5)
        run_cipher()
    if user == "no":
        print("\nHaha! That's what I thought!")
        exit()
    else:
        print("""PLEASE ENTER EITHER 'yes' or 'no'""")
        error()

# Error is for the mistake in the user input
# ======================================================================================================================
def error():
    user = input("""Are you ready to run the program? ('yes' OR 'no')""")
    if user == "yes":
        run_cipher()
    if user == "no":
        exit()
    else:
        error()

# Main function
# ======================================================================================================================
def run_cipher():

    # Defining the Variables
    # ==================================================================================================================
    print("""\n\033[1;31mWARNING\033[0m This code's unbreakable!\n""")
    temp = input("Input your message:\n").lower()
   
    # Substitution Cipher
    # ==================================================================================================================
    final = temp.replace("a"," 1 ")
    final = final.replace("b"," 2 ")
    final = final.replace("c"," 3 ")
    final = final.replace("d"," 4 ")
    final = final.replace("e"," 5 ")
    final = final.replace("f"," 6 ")
    final = final.replace("g"," 7 ")
    final = final.replace("h"," 8 ")
    final = final.replace("i"," 9 ")
    final = final.replace("j"," 0 ")
    final = final.replace("k"," 10 ")
    final = final.replace("l"," 11 ")
    final = final.replace("m"," 12 ")
    final = final.replace("n"," 13 ")
    final = final.replace("o"," 14 ")
    final = final.replace("p"," 15 ")
    final = final.replace("q"," 16 ")
    final = final.replace("r"," 17 ")
    final = final.replace("s"," 18 ")
    final = final.replace("t"," 19 ")
    final = final.replace("u"," 20 ")
    final = final.replace("v"," 21 ")
    final = final.replace("w"," 22 ")
    final = final.replace("x"," 23 ")
    final = final.replace("y"," 24 ")
    final = final.replace("z"," 25 ")
    final = final.replace(" 1 ", "z")
    final = final.replace(" 2 ", "y")
    final = final.replace(" 3 ", "x")
    final = final.replace(" 4 ", "w")
    final = final.replace(" 5 ", "v")
    final = final.replace(" 6 ", "u")
    final = final.replace(" 7 ", "t")
    final = final.replace(" 8 ", "s")
    final = final.replace(" 9 ", "r")
    final = final.replace(" 0 ", "q")
    final = final.replace(" 10 ", "p")
    final = final.replace(" 11 ", "o")
    final = final.replace(" 12 ", "n")
    final = final.replace(" 13 ", "m")
    final = final.replace(" 14 ", "l")
    final = final.replace(" 15 ", "k")
    final = final.replace(" 16 ", "j")
    final = final.replace(" 17 ", "i")
    final = final.replace(" 18 ", "h")
    final = final.replace(" 19 ", "g")
    final = final.replace(" 20 ", "f")
    final = final.replace(" 21 ", "e")
    final = final.replace(" 22 ", "d")
    final = final.replace(" 23 ", "c")
    final = final.replace(" 24 ", "b")
    final = final.replace(" 25 ", "a")

    # Mirror Cipher
    # ==================================================================================================================
    encrypted = ""
    for character in final:
        encrypted = character + encrypted
    print(final)

    # Odd and Even Number Cipher
    # ==================================================================================================================

    evenChars = ""
    oddChars = ""

    charCount = 0
    for char in final:
        if charCount % 2 is 0:
            # evens
            evenChars = evenChars + char
        if charCount % 2 is 1:
            # odds
            oddChars = oddChars + char

        charCount += 1

    cipherText = oddChars + evenChars

    # Results
    # ==================================================================================================================
    print("Your Results:\nYour original message of\033[1;34m", temp, "\033[0mis now encrypted into the message of\033[1;31m", cipherText, "\033[0m")

    # Asking the user whether to run the program again
    # ==================================================================================================================
    user_q = input("Would you like to encrypt something again?\n")
    if user_q == "yes":
        run_cipher()
    if user_q == "no":
        exit()
        
intro()

