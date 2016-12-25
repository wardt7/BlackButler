#!/usr/bin/python
# -*- coding: UTF-8 -*-
import hashlib, string
from random import SystemRandom


class Cipher:
    def __init__(self, alphabet="abcdefghijklmnopqrstuvwxyzぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんゔゕゖ゙゚゛゜ゝゞゟ゠ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶヷヸヹヺ・ーヽヾヿABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890<> !?"):
        if alphabet != "":
            self.ALPHABET = alphabet
        else:
            self.ALPHABET = "abcdefghijklmnopqrstuvwxyzぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんゔゕゖ゙゚゛゜ゝゞゟ゠ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶヷヸヹヺ・ーヽヾヿABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890<> !?"

    def get_ALPHABET(self):
        return self.ALPHABET

    def encode_caesar(self, message, offset):
        """Encodes a message using the caesar method. Offset indicates how much the alphabet is shifted by; a value
        of 0 results in no shift."""
        # Data Validation to make sure message entered can be used
        if message == "":
            return "Error: No characters were entered into the message field"
        for i in message:
            if self.ALPHABET.find(i) == -1:
                return "Error: At least one (1) character in message is not present in the alphabet\nused"
        try:
            offset = int(offset)
        # Data Validation to make sure offset can be used
        except ValueError:
            return "Error: The value for offset entered is not an integer"
        if offset < 0:
            return "Error: The value for offset is less than 0"
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
        # Data Validation to make sure message entered can be used
        if message == "":
            return "Error: No characters were entered into the message field"
        for i in message:
            if self.ALPHABET.find(i) == -1:
                return "Error: At least one (1) character in message is not present in the alphabet used"
        try:
            offset = int(offset)
        # Data Validation to make sure offset can be used
        except TypeError:
            return "Error: The value for offset entered is not an integer"
        if offset < 0:
            return "Error: The value for offset is less than 0"
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
        # Data Validation to make sure message entered can be used
        if message == "":
            return "Error: No characters were entered into the message field"
        for i in message:
            if self.ALPHABET.find(i) == -1:
                return "Error: At least one (1) character in message is not present in the alphabet\nused"
        # Data Validation to make sure keyword entered can be used
        if keyword == "":
            return "Error: No characters were entered into the keyword field"
        for i in keyword:
            if self.ALPHABET.find(i) == -1:
                return "Error: At least one (1) character in keyword is not present in the alphabet\nused"
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
        # Data Validation to make sure message entered can be used
        if message == "":
            return "Error: No characters were entered into the message field"
        for i in message:
            if self.ALPHABET.find(i) == -1:
                return "Error: At least one (1) character in message is not present in the alphabet\nused"
        # Data Validation to make sure keyword entered can be used
        if keyword == "":
            return "Error: No characters were entered into the keyword field"
        for i in keyword:
            if self.ALPHABET.find(i) == -1:
                return "Error: At least one (1) character in keyword is not present in the alphabet\nused"
        string_to_return = ""
        # Extends the keyword so that it is of the same length as message
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
            string_to_return += Cipher.decode_caesar(self, letter_message, letter_keyword_index)
        return string_to_return

class Morse(Cipher):
    def __init__(self):
        self.ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモヤユヨラリルレロワヰンヱヲ゛゜ーュャョガギグゲゴザジズゼゾダヂヅデドバビブベボパピプペポ \t\n."

    def encode_morse(self, message):
        """Encodes a message using Morse (International) and Wabun Code. Words are separated with the "/" symbol,
        while letters are separated with two spaces, and japanese characters with diacritics have one space
        between the letter and the diacritic used. Japanese digraphs are separated into two separate characters."""
        # Data Validation to make sure message entered can be used
        if message == "":
            return "Error: No characters were entered into the message field"
        for i in message:
            if self.ALPHABET.find(i) == -1:
                return "Error: At least one (1) character in message is not present in the alphabet\nused"
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
            # Makes the letter uppercase, as the MorseLatinCode.txt file contains comparisons for upper case letters
            # only
            letter_next = letter_next.capitalize()
            if letter_next.isspace():
                # The "/" character indicates that it is a space character to a decoder and not
                # just space to separate morse code characters
                string_to_return += "/  "
            elif letter_next == ".":
                # Prosign for new message (end of message/sentence)
                string_to_return += ".-.-.  "
            else:
                string_to_add = ""
                # We check if there has been a change of language (English <-> Japanese Katakana)
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
        # Data validation to make sure a valid morse message is present
        if message == "":
            return "Error: No characters were entered into the message field"
        for i in message:
            if " .-/".find(i) == -1:
                return "Error: At least one (1) character in message is not present in the alphabet\nused"
        string_to_return = ""
        # Loads in the WabunCode.txt and MorseLatinCode.txt files
        file_wabun = open("WabunCode.txt","r", encoding="UTF-8")
        file_morse = open("MorseLatinCode.txt","r", encoding="UTF-8")
        wabun = file_wabun.read()
        morse = file_morse.read()
        file_wabun.close()
        file_morse.close()
        # We presume that we start with Morse code first and then change once we see the first character. Note that
        # some sets of characters are in both wabun and morse and therefore have different meanings, so we must identify
        # whether or not japanese or english has been used.
        wabun_on = False
        while len(message) != 0:
            string_to_find = ""
            space_check = 0
            # We find the first set of characters to analyze. If there are more than two spaces after a character
            # or length is 0, then we've reached the end of that character set
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
            # Removes the set of characters we just found from the message
            message = message[len(string_to_find):]
            # Removes the space from the end of the set of characters we just found so that we can analyze them
            string_to_find = string_to_find.rstrip()
            # Checks to see if the set of characters is an exceptional set not found in either morse or wabun, such
            # as prosigns and backslash characters
            if string_to_find == "/":
                string_to_return += " "
            elif string_to_find == ".-.-." and wabun_on == False:
                # Wabun has to be false as there is a wabun character which matches this prosign
                string_to_return += "."
            elif string_to_find == "-..---":
                wabun_on = True
            elif string_to_find == "...-.":
                wabun_on = False
            else:
                # Looks for the set of characters in wabun if it is identified to be japanese, else looks for it
                # in morse.
                if wabun_on:
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

class PassGen():
    def __init__(self):
        self.ALPHABET = "abcdefghijklmnopqrstuvwxyzぁあぃいぅうぇえぉおかがきぎくぐけげこごさざしじすずせぜそぞただちぢっつづてでとどなにぬねのはばぱひびぴふぶぷへべぺほぼぽまみむめもゃやゅゆょよらりるれろゎわゐゑをんゔゕゖ゙゚゛゜ゝゞゟ゠ァアィイゥウェエォオカガキギクグケゲコゴサザシジスズセゼソゾタダチヂッツヅテデトドナニヌネノハバパヒビピフブプヘベペホボポマミムメモャヤュユョヨラリルレロヮワヰヱヲンヴヵヶヷヸヹヺ・ーヽヾヿABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890<> !?"

    def encode_zodiac64(self, keyword):
        """For use in keyword based ciphers - extends the length of a used keyword to 64 characters by using SHA-512
        hash functions to create a "Base-256" number, mainly to prevent the use of a Kasiski Examination."""
        # Data Validation to make sure keyword entered can be used
        if keyword == "":
            return "Error: No characters were entered into the keyword field"
        for i in keyword:
            if self.ALPHABET.find(i) == -1:
                return "Error: At least one (1) character in keyword is not present in the alphabet\nused"
        string_to_return = ""
        # Hashes the keyword and converts into a binary number
        keyword_hash = hashlib.sha512(keyword.encode()).hexdigest()
        keyword_binary = bin(int(keyword_hash, 16))[2:].zfill(512)
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
        try:
            length = int(length)
        # Data Validation to make sure length can be used
        except ValueError:
            return "Error: The value for length entered is not an integer"
        if length < 0:
            return "Error: The value for length is less than 0"
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
        # This is created so that one variable's data can be transferred to another
        self.frequency = {}

    def analyze(self,message):
        """Analyzes a message and finds the percentages of letters present"""
        # We specify some characters that we don't want included in the frequency analysis, and force all letters
        # to be uppercase so that there aren't duplicate letters (such as "A" and "a" being recognised as two different
        # characters
        ignore = string.whitespace+string.punctuation
        message = message.upper()
        for letter in message:
            # Checks if the letter is in the ignore variable
            if letter in ignore:
                pass
            # Checks to see if the letter has been found previously - if not, makes a new key
            elif letter not in self.frequency.keys():
                self.frequency[letter] = 1
            else:
                self.frequency[letter] += 1
        # Returns a different function which formats the output for a human to read
        return FreqAnalyzer.frequencies(self)

    def frequencies(self):
        """Formats the dictionary so that it is easy for a human to read"""
        output = ""
        # Converts the dictionary made held @ self.frequency into a list of tuples. This is so that the keys and values
        # can be manipulated. These are then swapped around
        sorted_freq = sorted([(value,key) for (key,value) in self.frequency.items()])
        sorted_freq.reverse()
        # The program then proceeds to use a formatting function to organise the output so it can be read easily
        output += "Letter\t Frequency\n"
        for pairs in sorted_freq:
            output += "{}:\t\t{}\t\n".format(pairs[1],pairs[0])
        return output



