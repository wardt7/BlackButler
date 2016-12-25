#!/usr/bin/python
# -*- coding: UTF-8 -*-
import hashlib, string
from random import SystemRandom


class Cipher:
    def __init__(self, alphabet="abcdefghijklmnopqrstuvwxyzぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんゔゕゖ゙゚゛゜ゝゞゟ゠ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶヷヸヹヺ・ーヽヾヿABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890<> !?"):
        self.ALPHABET = alphabet

    def get_ALPHABET(self):
        return self.ALPHABET

    def encode_caesar(self, message, offset):
        """Encodes a message using the caesar method. Offset indicates how much the alphabet is shifted by; a value
        of 0 results in no shift."""
        string_to_return = ""
        # Creates a shifted alphabet based on offset
        shifted_alphabet = self.ALPHABET[offset:] + self.ALPHABET[:offset + 2]
        for letter in message:
            if letter.isspace():
                string_to_return += " "
            else:
                # Looks at the location the letters in the message are in the alphabet
                shifted_letter_index = self.ALPHABET.find(letter)
                # Uses the found index above and searches the shifted_alphabet for the new letter
                shifted_letter = shifted_alphabet[shifted_letter_index]
                # Adds the letter to the returned string
                string_to_return += shifted_letter
        return string_to_return

    def decode_caesar(self, message, offset):
        """Decodes a message using the caesar method. Offset indicates how much the alphabet was shifted by during the
        encoding process; a value of 0 results in no shift."""
        string_to_return = ""
        # Creates a shifted alphabet based on offset
        shifted_alphabet = self.ALPHABET[offset:] + self.ALPHABET[:offset + 2]
        for letter in message:
            if letter.isspace():
                string_to_return += " "
            else:
                # Looks at the location the letters in the message are in the shifted_alphabet
                original_letter_index = shifted_alphabet.find(letter)
                # Uses the found index above and searches the alphabet for the original letter
                original_letter = self.ALPHABET[original_letter_index]
                # Adds the letter to the returned string
                string_to_return += original_letter
        return string_to_return

    def encode_vignere(self, message, keyword):
        """Encodes a message using the vignere method, which incorporates the caesar method. The keyword is used to
        determine the offset of each letter"""
        string_to_return = ""
        # The keyword length must be the same as the message length in order for the system to work
        while len(keyword) != len(message):
            if len(keyword) > len(message):
                keyword = keyword[:len(message)]
            else:
                keyword += keyword
        for index in range(len(message)):
            # Looks at where the letter chosen from the keyword is in the alphabet. This is the offset which will be
            # used when the caesar method is called.
            letter_message = message[index]
            letter_keyword = keyword[index]
            letter_keyword_index = self.ALPHABET.find(letter_keyword)
            string_to_return += Cipher.encode_caesar(self, letter_message, letter_keyword_index)
        return string_to_return

    def decode_vignere(self, message, keyword):
        """Decodes a message using the vignere method. This is essentially the same as the encode_vignere method,
        except that it uses Cipher.decode_caesar instead of Cipher.encode_caesar."""
        string_to_return = ""
        while len(keyword) != len(message):
            if len(keyword) > len(message):
                keyword = keyword[:len(message)]
            else:
                keyword += keyword
        for index in range(len(message)):
            letter_message = message[index]
            letter_keyword = keyword[index]
            letter_keyword_index = self.ALPHABET.find(letter_keyword)
            string_to_return += Cipher.decode_caesar(self, letter_message, letter_keyword_index)
        return string_to_return

    def encode_railfence(self, message, offset):
        """Encodes a message using the railfence method, which splits up the message using a series of "rails" and
        then putting them back together again"""
        rails = []
        for i in range(offset):
            # We need to create strings before we can append letters
            rails.append("")
        string_to_return = ""
        while len(message) != 0:
            for i in range(offset):
                if len(message) == 0:
                    # Required as otherwise the program will stop working
                    break
                else:
                    rails[i] += message[0]
                    message = message[1:]
        for i in range(offset):
            string_to_return += rails[i]
        return string_to_return

    def decode_railfence(self, message, offset):
        rails = []
        for i in range(offset):
            rails.append("")
        string_to_return = ""
        while len(message) != 0:
            for i in range(offset):
                try:
                    rails[i] += message[i]
                except IndexError:
                    message = ""
                    break
                if i == (offset-1):
                    message = message[offset:]
        for i in range(offset):
            string_to_return += rails[i]
        return string_to_return


class Morse(Cipher):
    def __init__(self):
        self.ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヰンヱヲ゛゜ーュャョガギグゲゴザジズゼゾダヂヅデドバビブベボパピプペポ \t\n."

    def encode_morse(self, message):
        """Encodes a message using Morse (International) and Wabun Code. Words are separated with the "/" symbol,
        while letters are separated with two spaces, and japanese characters with diacritics have one space
        between the letter and the diacritic used. Japanese digraphs are separated into two separate characters."""
        # We need a way of tracking which characters are latin and which are japanese, as we must include additional
        # characters in order to signify this change (referred to as prosigns).
        letter_previous = ""
        string_to_return = ""
        # Reads the entirety of WabunCodeEncode.txt and MorseLatinCodeEncode.txt
        file_wabun = open("WabunCode.txt","r", encoding="UTF-8")
        file_morse = open("MorseLatinCode.txt","r", encoding="UTF-8")
        wabun = file_wabun.read()
        morse = file_morse.read()
        file_wabun.close()
        file_morse.close()
        for letter_next in message:
            letter_next = letter_next.capitalize()
            if letter_next.isspace():
                string_to_return += "/  "
            elif letter_next == ".":
                # Prosign for new message (end of message/sentence)
                string_to_return += ".-.-.  "
            else:
                string_to_add = ""
                if not letter_previous.isspace():
                    if (morse.find(letter_previous) != -1 or letter_previous == "") and wabun.find(letter_next) != -1:
                        # Prosign for changing from Morse to Wabun
                        string_to_add += "-..---  "
                    if morse.find(letter_next) != -1 and wabun.find(letter_previous) != -1 and letter_previous != "":
                        # Prosign for changing from Wabun to Morse
                        string_to_add += "...-.  "
                # Looks for the corresponding Morse/Wabun code from the text files
                morse_index = morse.find(letter_next)
                if morse_index != -1:
                    morse_index += 4
                    # The Morse/Wabun code vary in length, but all end with the "\n" character, which is what
                    # is used as a condition for termination
                    while morse[morse_index] != "\n":
                        string_to_add += morse[morse_index]
                        morse_index += 1
                else:
                    # Similar method to the above but looks in wabun instead of morse.
                    wabun_index = wabun.find(letter_next)
                    wabun_index += 4
                    while wabun[wabun_index] != "\n":
                        string_to_add += wabun[wabun_index]
                        wabun_index += 1
                string_to_return += string_to_add.rstrip()+"  "
                # This variable does not include spaces and the full stop (.) as valid data.
                letter_previous = letter_next
        # Tidies up the string so there's no additional whitespace at the end (saves characters)
        return string_to_return

    def decode_morse(self, message):
        """Decodes a message from Morse/Wabun code to English/Japanese"""
        string_to_return = ""
        file_wabun = open("WabunCode.txt","r", encoding="UTF-8")
        file_morse = open("MorseLatinCode.txt","r", encoding="UTF-8")
        wabun = file_wabun.read()
        morse = file_morse.read()
        file_wabun.close()
        file_morse.close()
        wabun_on = False
        while len(message) != 0:
            string_to_find = ""
            space_check = 0
            for letter in message:
                if len(message) == 0 or space_check == 2:
                    break
                elif letter == "/":
                    string_to_find += "/  "
                    break
                elif letter == " ":
                    space_check += 1
                    string_to_find += letter
                else:
                    string_to_find += letter
                    space_check = 0
            message = message[len(string_to_find):]
            string_to_find = string_to_find.rstrip()
            if string_to_find == "/":
                string_to_return += " "
            elif string_to_find == ".-.-.":
                string_to_return += "."
            elif string_to_find == "-..---":
                wabun_on = True
            elif string_to_find == "...-.":
                wabun_on = False
            else:
                if wabun_on:
                    #FIXME: Need to check the while loop works ok.
                    while len(string_to_find) != 10:
                        string_to_find += " "
                    wabun_index = wabun.find(string_to_find)-4
                    string_to_return += wabun[wabun_index]
                else:
                    while len(string_to_find) != 5:
                        string_to_find += " "
                    string_to_find += "\n"
                    morse_index = morse.find(string_to_find)-4
                    string_to_return += morse[morse_index]
        return string_to_return

class PassGen(Cipher):
    def __init__(self):
        self.ALPHABET = "abcdefghijklmnopqrstuvwxyzぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんゔゕゖ゙゚゛゜ゝゞゟ゠ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶヷヸヹヺ・ーヽヾヿABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890<> !?"

    def encode_zodiac64(self, keyword):
        """For use in keyword based ciphers - extends the length of a used keyword to 64 characters by using SHA-512
        hash functions to create a "Base-256" number, mainly to prevent the use of a Kasiski Examination.
        Probably needs a way of including a salt (sign in?). "Invented" by Toby Ward"""
        string_to_return = ""
        # Hashes the keyword and converts into a binary number
        keyword_hash = hashlib.sha512(keyword.encode()).hexdigest()
        keyword_binary = bin(int(keyword_hash, 16))[2:].zfill(512)
        print(keyword_binary)
        while len(keyword_binary) != 0:
            # Takes out the first byte in keyword_binary and converts to decimal to create an index
            index = int(keyword_binary[:8], 2)
            # Removes the found byte from the overall string
            keyword_binary = keyword_binary[8:]
            # Converts to Base-256 by searching the alphabet using the given index
            keyword_letter = self.ALPHABET[index]
            string_to_return += keyword_letter
        return string_to_return

    def encode_zodiac128(self, keyword1, keyword2):
        """Extends the zodiac64 encoding to 128 characters by using 2 keywords"""
        string_to_return = ""
        keywords = [keyword1, keyword2]
        for i in range(2):
            string_to_return += PassGen.encode_zodiac64(self, keywords[i])
        return string_to_return

    def encode_zodiac256(self, keyword1, keyword2, keyword3, keyword4):
        """Extends the zodiac64 encoding to 256 by using 4 keywords"""
        string_to_return = ""
        keywords = [keyword1, keyword2, keyword3, keyword4]
        for i in range(4):
            string_to_return += PassGen.encode_zodiac64(self, keywords[i])
        return string_to_return

    @staticmethod
    def encode_diceware(length):
        """Generates a password with strong entropy by using dicerolls and a dictionary.
        Length represents how long the desired password should be. For license details regarding
        to the supplied diceware.txt file used, see the LICENSE.txt file."""
        string_to_return = ""
        roll = ""
        # A SystemRandom object is created here - we use this as it's more cryptographically secure - especially
        # pertinent with the One Time Pad cipher.
        cryptogen = SystemRandom()
        # Loads in the diceware details from diceware.txt
        diceware_file = open("diceware.txt", "r")
        diceware = diceware_file.read()
        diceware_file.close()
        while len(string_to_return) < length:
            # Generates a roll set to use
            for i in range(5):
                roll += str(cryptogen.randrange(1, 6))
            # Finds the rollset in the diceware file
            index = diceware.find(roll)
            for j in range(6):
                # Adds characters to the string to return until it reaches a \n character
                character = diceware[(index + 6) + j]
                if character == "\n":
                    break
                else:
                    roll = ""
                    string_to_return += character
        # Shortens the length of the string to return to the user's desired length
        if len(string_to_return) > length:
            string_to_return = string_to_return[:length + 1]
        return string_to_return

class FreqAnalyzer:
    def __init__(self):
        self.frequency = {}

    def analyze(self,message):
        """Analyzes a message and finds the percentages of letters present"""
        self.frequency={}
        ignore = string.whitespace+string.punctuation
        message = message.upper()
        for letter in message:
            # Does not include whitespace types in
            if letter in ignore:
                pass
            # Checks to see if the letter has been found previously - if not, makes a new key
            elif letter not in self.frequency.keys():
                self.frequency[letter] = 1
            else:
                self.frequency[letter] += 1
        return FreqAnalyzer.frequencies(self)

    def frequencies(self):
        """Turns the frequency into a lovely output"""
        output = ""
        # Converts the dictionary made @ self.frequency into a list of tuples. This is so that the keys and values
        # can be manipulated
        sorted_freq = sorted([(value,key) for (key,value) in self.frequency.items()])
        sorted_freq.reverse()
        output += "Letter\tFrequency\n"
        for pairs in sorted_freq:
            output += "{}:\t\t{}\t\n".format(pairs[1],pairs[0])
        return output

cipher = Cipher()
print(cipher.decode_railfence("afbcde", 5
))






