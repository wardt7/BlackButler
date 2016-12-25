__author__ = 'WardT'
import cipher
from tkinter import *
from tkinter import ttk
from tkinter import font
#pytumblr


class Interface:
    def __init__(self):
        """Initiates the main menu and sets variables which will be used across multiple windows"""
        self.mainmenu = Tk()
        # Sets some default fonts for use in the program's theme
        self.font_headings = font.Font(family="Helvetica", size=14)
        self.font_title = font.Font(family="Helvetica", size=32, weight="bold")
        self.font_text = font.Font(family="Helvetica", size=12)
        # Variables used to store the user's social media details required for posting to social media
        self.client_public_key = ""
        self.client_private_key = ""
        self.oauth_public = ""
        self.oauth_private = ""
        self.blog_name = ""
        self.options_menu_errors = ""
        # Creates variables which store the options which the user defines for use in the program
        self.encipher_options_alpha_info = StringVar()
        self.encipher_options_keyword_info = StringVar()
        self.encipher_options_offset_info = StringVar()
        self.encipher_options_tumblr_tags_info = StringVar()
        self.encipher_options_tumblr_url_info = StringVar()
        self.pass_options_keyword_one_info = StringVar()
        self.pass_options_keyword_two_info = StringVar()
        self.pass_options_keyword_three_info = StringVar()
        self.pass_options_keyword_four_info = StringVar()
        self.pass_options_length_info = StringVar()
        self.pass_names = ("Zodiac64", "Zodiac128", "Zodiac256", "Diceware")
        self.pass_descriptions = {(0,): """The Zodiac series of password generators use hashing algorithms to generate a password
        for use in BlackButler using both latin and japanese characters.
        You Must Include:
            - Keywords containing characters any amount of characters from Uppercase and
            Lowercase English,numbers 0-9, Japanese (Katakana and Hiragana, including
            diacritic marks), and a space (NOT Enter/Tab/etc.)""", (1,):
        """The Zodiac series of password generators use hashing algorithms to
        generate a password for use in BlackButler using both latin and japanese characters.
        You Must Include:
            - Keywords containing characters any amount of characters from Uppercase and Lowercase English,
        numbers 0-9, Japanese (Katakana and Hiragana, including diacritic marks), and a space (NOT Enter/Tab/etc.)""", (2,):
        """The Zodiac series of password generators use hashing algorithms to
        generate a password for use in BlackButler using both latin and japanese characters.
        You Must Include:
            - Keywords containing characters any amount of characters from Uppercase and Lowercase English,
        numbers 0-9, Japanese (Katakana and Hiragana, including diacritic marks), and a space (NOT Enter/Tab/etc.)""", (3,):
        """The diceware password generator creates a password containing latin characters by
        randomly generating a number and comparing this to a word in a given dictionary,
        and adding this to an output until a desired length is reached.
        You Must Include:
            - A length larger than 0 that is also an integer"""}
        self.cipher_names = ("Caesar", "Vignere", "Morse")
        self.cipher_descriptions = {(0,): """The Caesar cipher, also known as Caesar's cipher, the shift cipher,
        Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques. It is a type
        of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of
        positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B,
        and so on. The method is named after Julius Caesar, who used it in his private correspondence.
        You must include:
        - An offset larger than or equal to 0, which is also an integer (whole)
        - A message containing letters used in your chosen alphabet
        You may also:
        - Assign your own alphabet to be used. The default alphabet contains Uppercase and Lowercase English,
        numbers 0-9, Japanese (Katakana and Hiragana, including diacritic marks), and a space (NOT Enter/Tab/etc.)""",
                                   (1,):
        """The Vigenère cipher is a method of encrypting alphabetic text by using a series of different Caesar ciphers
        based on the letters of a keyword. It is a simple form of polyalphabetic substitution.
        You must include:
        - A message and keyword containing letters used in your chosen alphabet
        You are advised that:
        - In order to be fully secure, you must use a keyword of equal length to the message.
        You may also:
        - Assign your own alphabet to be used. The default alphabet contains Uppercase and Lowercase English,
        numbers 0-9, Japanese (Katakana and Hiragana, including diacritic marks), and a space (NOT Enter/Tab/etc.)""",
                                   (2,): """Morse code is a method of transmitting text information as a series of on-off tones, lights, or
        clicks that can be directly understood by a skilled listener or observer without special equipment.
        You must include:
        - A message containing any amount of Uppercase and Lowercase English, numbers 0-9, Japanese (Katakana and
        diacritics ONLY)
        - When decoding, \"-..---\" at the start of the message if you believe the message starts with Japanese
        characters
        You must also, when decoding:
        - Separate letters with two spaces
        - Separate words with two spaces and a backslash (\) character"""}
        ttk.Style().configure(style="TButton", font=self.font_text)
        ttk.Style().configure(style="TFrame", background="White")
        ttk.Style().configure(style="TLabel", background="White")


    def main_menu(self):
        # Set up the actual window by giving it a title and grid
        self.mainmenu.title("BlackButler - Main Menu")
        self.mainmenu.columnconfigure(0, weight=1)
        self.mainmenu.rowconfigure(0, weight=1)
        self.mainmenu["background"] = "White"
        # Creates a frame to hold all other frames so that when the window is expanded, all widgets stay central to
        # the window
        holding_frame = ttk.Frame(self.mainmenu)
        holding_frame.grid(column=0, row=0)
        # Add in labels
        title = ttk.Label(holding_frame, text="BlackButler", font=self.font_title, padding=5)
        title.grid(column=2, row=1, sticky=())
        describe = ttk.Label(holding_frame, text="A program for enciphering, deciphering, and cracking messages and passwords", font=self.font_headings, padding=5)
        describe.grid(column=1, row=2, columnspan=3, sticky=(N,S))
        # Buttons for accessing the different parts of the program
        encipher_button = ttk.Button(holding_frame, text="Encipherer and Decipherer", command=self.encipher_decipher,  padding=5, width=25)
        encipher_button.grid(column=1, row=3, sticky=(N,E,S,W))
        pass_generator_button = ttk.Button(holding_frame, text="Password Generator", command=self.pass_generator, padding=5, width=25)
        pass_generator_button.grid(column=3,row=3, sticky=(N,E,S,W))
        frequency_analysis_button = ttk.Button(holding_frame, text="Frequency Analyser", command=self.frequency_analyzer, padding=5, width=25)
        frequency_analysis_button.grid(column=1, row=5, sticky=(N,E,S,W))
        options_settings_button = ttk.Button(holding_frame, text="Options and Settings", command=self.options_settings, padding=5, width=25)
        options_settings_button.grid(column=3, row=5, sticky=(N,E,S,W))
        self.mainmenu.mainloop()

    def encipher_decipher(self):
        # Creates a new window for the Enciphering Screen
        encipher_screen = Toplevel()
        encipher_screen.title("BlackButler - Encipher and Decipher")
        encipher_screen.columnconfigure(0, weight=1)
        encipher_screen.rowconfigure(0, weight=1)
        # Creates a frame to hold all other frames so that when the window is expanded, all widgets stay central to
        # the window
        holding_encipher_frame = ttk.Frame(encipher_screen)
        holding_encipher_frame.grid(column=0, row=0)
        # Creates a frame which will contain a text box and a listbox
        encipher_describe_frame = ttk.Frame(holding_encipher_frame)
        encipher_describe_frame.grid(column=0, row=0,sticky=(E,W))
        encipher_describe_frame["padding"] = (5,5)
        encipher_describe_frame["borderwidth"] = 2
        # Specifies the style of border for the frame
        encipher_describe_frame["relief"] = "solid"
        encipher_describe_title = ttk.Label(encipher_describe_frame, text="Ciphering Methods", font=self.font_headings)
        encipher_describe_title.grid(column=1, row=0)
        # Creates a description box to hold the description of the cipher selected
        global encipher_description_box
        encipher_description_box = Text(encipher_describe_frame, width=70,height=20, font=self.font_text, state="disabled", background="White")
        encipher_description_box.grid(column=1, row=1, columnspan=2)
        # Creates a listbox which contains the ciphers available to the user
        encipher_methods_selection = Listbox(encipher_describe_frame, height=19, font=self.font_text)
        for item in self.cipher_names:
            encipher_methods_selection.insert(END,item)
        encipher_methods_selection.grid(column=0, row=1)
        encipher_methods_selection.bind("<<ListboxSelect>>", lambda event: self.encipher_decipher_select(encipher_methods_selection.curselection()))
        # Creates a frame which will contain entry boxes for inputting data
        encipher_options_frame = ttk.Frame(holding_encipher_frame)
        encipher_options_frame.grid(column=1,row=0, sticky=(N,S,E,W))
        encipher_options_frame["padding"] = (5,5)
        encipher_options_frame["borderwidth"] = 2
        encipher_options_frame["relief"] = "solid"
        # Creates a title for the options frame
        encipher_options_title = ttk.Label(encipher_options_frame, text="Required Information", font=self.font_headings, padding=5)
        encipher_options_title.grid(column=1, row=0, sticky=N)
        # Creates the labels for the options available
        encipher_options_alpha_label = ttk.Label(encipher_options_frame, text="Alternative Alphabet", font=self.font_text, padding=5)
        encipher_options_alpha_label.grid(column=0, row=1)
        encipher_options_keyword_label = ttk.Label(encipher_options_frame, text="Keyword", font=self.font_text, padding=5)
        encipher_options_keyword_label.grid(column=0, row=2)
        encipher_options_offset_label = ttk.Label(encipher_options_frame, text="Offset", font=self.font_text, padding=5)
        encipher_options_offset_label.grid(column=0, row=3)
        encipher_options_tumblr_tags_label = ttk.Label(encipher_options_frame, text="Tumblr Tags", font=self.font_text, padding=(5,10))
        encipher_options_tumblr_tags_label.grid(column=0, row=5)
        encipher_options_tumblr_url_label = ttk.Label(encipher_options_frame, text="Tumblr URL", font=self.font_text, padding=5)
        encipher_options_tumblr_url_label.grid(column=0,row=4)
        # Creates entry boxes for some of the options available
        global encipher_options_alpha_entry, encipher_options_keyword_entry
        encipher_options_alpha_entry = ttk.Entry(encipher_options_frame, textvariable=self.encipher_options_alpha_info, font=self.font_text, width=40)
        encipher_options_alpha_entry.grid(column=1, row=1, columnspan=2)
        encipher_options_keyword_entry = ttk.Entry(encipher_options_frame, textvariable=self.encipher_options_keyword_info, font=self.font_text, width=40)
        encipher_options_keyword_entry.grid(column=1, row=2, columnspan=2)
        encipher_options_tumblr_tags_entry = ttk.Entry(encipher_options_frame, textvariable=self.encipher_options_tumblr_tags_info, font=self.font_text, width=40)
        encipher_options_tumblr_tags_entry.grid(column=1, row=5, columnspan=2)
        encipher_options_tumblr_url_entry = ttk.Entry(encipher_options_frame, textvariable=self.encipher_options_tumblr_url_info, font=self.font_text, width=40)
        encipher_options_tumblr_url_entry.grid(column=1, row=4, columnspan=2)
        # Creates the spinbox for one of the options
        global encipher_options_offset_spin
        encipher_options_offset_spin = Spinbox(encipher_options_frame, from_=0, to=float("inf"), increment=1, textvariable=self.encipher_options_offset_info, font=self.font_text, width=39)
        encipher_options_offset_spin.grid(column=1, row=3, columnspan=2)
        # Creates the frame to hold the message input, message output and buttons for processing
        encipher_io_frame = ttk.Frame(holding_encipher_frame)
        encipher_io_frame.grid(column=0,row=1, columnspan=2, sticky=(E,W))
        encipher_io_frame["padding"] = (5,5)
        encipher_io_frame["borderwidth"] = 2
        encipher_io_frame["relief"] = "solid"
        # Creates the entry for users' messages
        encipher_io_input = Text(encipher_io_frame, font=self.font_text, width=80, height=20)
        encipher_io_input.grid(column=0,row=0,rowspan=3, sticky=E)
        # Creates the output box for users' messages
        global encipher_io_output
        encipher_io_output = Text(encipher_io_frame, font=self.font_text, width=60, height=20, state="disabled", background="White")
        encipher_io_output.grid(column=2, row=0, rowspan=3)
        # Creates the buttons for enciphering, deciphering, and posting to tumblr
        encipher_io_encipher = ttk.Button(encipher_io_frame, text="Encipher", command=lambda: self.encipher_decipher_process("encipher",encipher_methods_selection.curselection(), encipher_io_input.get("1.0", END)))
        encipher_io_encipher.grid(column=1,row=0,sticky=(E,W,N,S))
        encipher_io_decipher = ttk.Button(encipher_io_frame, text="Decipher", command=lambda: self.encipher_decipher_process("decipher",encipher_methods_selection.curselection(), encipher_io_input.get("1.0", END)))
        encipher_io_decipher.grid(column=1,row=1,sticky=(E,W,N,S))
        encipher_io_post = ttk.Button(encipher_io_frame, text="Post to Tumblr", command=lambda: self.encipher_decipher_process("tumblr",encipher_methods_selection.curselection(), encipher_io_output.get("1.0", END)))
        encipher_io_post.grid(column=1,row=2,sticky=(E,W,N,S))

    def pass_generator(self):
        # Creates a new window for the Password Generation Screen
        pass_screen = Toplevel()
        pass_screen.title("BlackButler - Password Generator")
        pass_screen.columnconfigure(0, weight=1)
        pass_screen.rowconfigure(0, weight=1)
        pass_screen_message = StringVar()
        # Creates a frame to hold all other frames so that when the window is expanded, all widgets stay central to
        # the window
        holding_pass_frame = ttk.Frame(pass_screen)
        holding_pass_frame.grid(column=0, row=0)
        # Creates a frame which will contain a text box and a listbox
        pass_describe_frame = ttk.Frame(holding_pass_frame)
        pass_describe_frame.grid(column=0, row=0,sticky=(E,W))
        pass_describe_frame["padding"] = (5,5)
        pass_describe_frame["borderwidth"] = 2
        # Specifies the style of border for the frame
        pass_describe_frame["relief"] = "solid"
        encipher_describe_title = ttk.Label(pass_describe_frame, text="Ciphering Methods", font=self.font_headings)
        encipher_describe_title.grid(column=1, row=0)
        # Creates a description box to hold the description of the password generation method selected
        global pass_description_box
        pass_description_box = Text(pass_describe_frame, width=70,height=20, font=self.font_text, state="disabled", background="White")
        pass_description_box.grid(column=1, row=1, columnspan=2)
        # Creates a listbox which contains the password generation methods available to the user
        pass_methods_selection = Listbox(pass_describe_frame, height=19, font=self.font_text)
        for item in self.pass_names:
            pass_methods_selection.insert(END,item)
        pass_methods_selection.grid(column=0, row=1)
        pass_methods_selection.bind("<<ListboxSelect>>", lambda event: self.pass_generator_select(pass_methods_selection.curselection()))
        # Creates a frame which will contain entry boxes for inputting data
        pass_options_frame = ttk.Frame(holding_pass_frame)
        pass_options_frame.grid(column=1,row=0, sticky=(N,S,E,W))
        pass_options_frame["padding"] = (5,5)
        pass_options_frame["borderwidth"] = 2
        pass_options_frame["relief"] = "solid"
        # Creates a title for the options frame
        pass_options_title = ttk.Label(pass_options_frame, text="Required Information", font=self.font_headings, padding=5)
        pass_options_title.grid(column=1, row=0, sticky=N)
        # Creates the labels for the options available
        pass_options_keyword_one_label = ttk.Label(pass_options_frame, text="Keyword 1", font=self.font_text, padding=5)
        pass_options_keyword_one_label.grid(column=0, row=1)
        pass_options_keyword_two_label = ttk.Label(pass_options_frame, text="Keyword 2", font=self.font_text, padding=5)
        pass_options_keyword_two_label.grid(column=0, row=2)
        pass_options_keyword_three_label = ttk.Label(pass_options_frame, text="Keyword 3", font=self.font_text, padding=5)
        pass_options_keyword_three_label.grid(column=0, row=3)
        pass_options_keyword_four_label = ttk.Label(pass_options_frame, text="Keyword 4", font=self.font_text, padding=(5,10))
        pass_options_keyword_four_label.grid(column=0, row=4)
        pass_options_length_label = ttk.Label(pass_options_frame, text="Length", font=self.font_text, padding=5)
        pass_options_length_label.grid(column=0,row=5)
        # Creates entry boxes for some of the options available
        global pass_options_keyword_one_entry,pass_options_keyword_two_entry,pass_options_keyword_three_entry,pass_options_keyword_four_entry
        pass_options_keyword_one_entry = ttk.Entry(pass_options_frame, textvariable=self.pass_options_keyword_one_info, font=self.font_text, width=40)
        pass_options_keyword_one_entry.grid(column=1, row=1, columnspan=2)
        pass_options_keyword_two_entry = ttk.Entry(pass_options_frame, textvariable=self.pass_options_keyword_two_info, font=self.font_text, width=40)
        pass_options_keyword_two_entry.grid(column=1, row=2, columnspan=2)
        pass_options_keyword_three_entry = ttk.Entry(pass_options_frame, textvariable=self.pass_options_keyword_three_info, font=self.font_text, width=40)
        pass_options_keyword_three_entry.grid(column=1, row=3, columnspan=2)
        pass_options_keyword_four_entry = ttk.Entry(pass_options_frame, textvariable=self.pass_options_keyword_four_info, font=self.font_text, width=40)
        pass_options_keyword_four_entry.grid(column=1, row=4, columnspan=2)
        # Creates the spinbox for one of the options
        global pass_options_length_spin
        pass_options_length_spin = Spinbox(pass_options_frame, from_=0, to=float("inf"), increment=1, textvariable=self.pass_options_length_info, font=self.font_text, width=39)
        pass_options_length_spin.grid(column=1, row=5, columnspan=2)
        # Creates the frame to hold the message output and password generation button
        pass_io_frame = ttk.Frame(holding_pass_frame)
        pass_io_frame.grid(column=0,row=1, columnspan=2, sticky=(E,W))
        pass_io_frame["padding"] = (5,5)
        pass_io_frame["borderwidth"] = 2
        pass_io_frame["relief"] = "solid"
        # Creates the buttons for enciphering, deciphering, and posting to tumblr
        pass_io_generate = ttk.Button(pass_io_frame, text="Encipher", command=lambda: self.pass_generator_process(pass_methods_selection.curselection()))
        pass_io_generate.grid(column=0,row=0,sticky=(E,W,N,S))
        # Creates the output box for users' messages
        global pass_io_output
        pass_io_output = Text(pass_io_frame, font=self.font_text, width=130, height=5, state="disabled", background="White")
        pass_io_output.grid(column=1, row=0)
    def frequency_analyzer(self):
        # Creates a new window for the Options and Settings Screen
        freq_screen = Toplevel()
        freq_screen.title("BlackButler - Frequency Analyzer")
        freq_screen.columnconfigure(0, weight1=1)
        freq_screen.rowconfigure(0, weight=1)
        # Creates a frame so that when the window is expanded, all widgets stay central to the window. Unlike other
        # windows, only one frame will be used in this screen
        holding_freq_frame = ttk.Frame(freq_screen)
        holding_freq_frame.grid(column=0, row=0)
        holding_freq_frame["padding"] = (5,5)
        holding_freq_frame["borderwidth"] = 2
        # Specifies the style of border for the frame
        holding_freq_frame["relief"] = "solid"
        # Creates a text box for users to enter their data
        global freq_input
        freq_input = Text(holding_freq_frame, font=self.font_text, width=60, height=30)
        freq_input.grid(column=0, row=0)
        # Creates a text box for outputs
        global freq_output
        freq_output = Text(holding_freq_frame, font=self.font_text, width=60, height=30, state="disabled")
        freq_output.grid(column=1, row=0)
        # Creates a button to process the given input
        freq_generate = ttk.Button(holding_freq_frame, text="Analyze Frequencies", command=lambda: self.frequency_analyzer_process(freq_input.get(1.0,END)))
        freq_generate.grid(column=2,row=0, sticky=(N,S))

    def options_settings(self):
        # Creates a new window for the Options and Settings Screen
        options_screen = Toplevel()
        options_screen.title("BlackButler - Options and Settings")
        options_screen.columnconfigure(0, weight=1)
        options_screen.rowconfigure(0, weight=1)
        # Creates a frame to hold all other frames so that when the window is expanded, all widgets stay central to
        # the window
        holding_options_frame = ttk.Frame(options_screen)
        holding_options_frame.grid(column=0, row=0)
        # Creates a frame which will contain entry boxes and labels
        contents_frame = ttk.Frame(holding_options_frame)
        contents_frame.grid(column=0, row=0)
        contents_frame["padding"] = (5,5)
        contents_frame["borderwidth"] = 2
        # Specifies the style of border for the frame
        contents_frame["relief"] = "solid"
        # Creates an invisible frame to hold other contents
        other_contents_frame = ttk.Frame(holding_options_frame)
        other_contents_frame.grid(column=0, row=1)
        other_contents_frame["padding"] = (5,5)
        # Create variables used to track entries in the entry boxes provided. Unlike other screens, these variables
        # are not class instances, as we will later save the contents of these in another variable (This is because
        # the contents of "StringVar()" are deleted when the screen is exited).
        client_public_contents = StringVar()
        client_private_contents = StringVar()
        blog_name_contents = StringVar()
        # Adds labels to the frame
        options_title = ttk.Label(contents_frame, text="Options and Settings", font=self.font_headings)
        options_title.grid(column=1, row=0)
        client_public_label = ttk.Label(contents_frame, text="Client Public Key", font=self.font_text, padding=5)
        client_public_label.grid(column=0,row=1, sticky=E)
        client_private_label = ttk.Label(contents_frame, text="Client Private Key", font=self.font_text, padding=5)
        client_private_label.grid(column=0,row=2, sticky=E)
        blog_name_label = ttk.Label(contents_frame, text="Blog Name", font=self.font_text, padding=5)
        blog_name_label.grid(column=0,row=3, sticky=E)
        # Adds entry boxes to the frame
        client_public_entry = ttk.Entry(contents_frame, textvariable=client_public_contents, font=self.font_text, width=50)
        client_public_entry.grid(column=1,row=1, columnspan=2, sticky=(E,W))
        client_private_entry = ttk.Entry(contents_frame, textvariable=client_private_contents, font=self.font_text, width=50)
        client_private_entry.grid(column=1,row=2, columnspan=2, sticky=(E,W))
        blog_name_entry = ttk.Entry(contents_frame, textvariable=blog_name_contents, width=50, font=self.font_text)
        blog_name_entry.grid(column=1,row=3, columnspan=2, sticky=(E,W))
        # Adds the save settings button
        save_button = ttk.Button(other_contents_frame,text="Save Settings", command=lambda: self.options_settings_save(client_public_contents.get(),client_private_contents.get(),blog_name_contents.get()), padding=5)
        save_button.grid(column=0, row=0)
        # Adds the error message text box
        global error_box
        error_box = Text(other_contents_frame,font=self.font_text, state="disabled", background="white", width=50, height=1)
        error_box.grid(column=1, row=0, sticky=W)
        options_screen.mainloop()

    def frequency_analyzer_process(self, message):
        """Frequency analyzes a given message by passing it to a FreqAnalyzer object and then outputting the result"""
        freq_object = cipher.FreqAnalyzer()
        output = freq_object.analyze(message[:len(message)-1])
        # Temporarily enables the output box and inserts the given output
        freq_output["state"] = "normal"
        freq_output.delete("1.0",END)
        freq_output.insert("1.0", output)
        freq_output["state"] = "disabled"

    def encipher_decipher_select(self,method):
        """Performs specific actions when an enciphering method is selected"""
        # Disable all of the options first, then enable the ones we don't want. We also delete any text present
        encipher_options_alpha_entry.state(["disabled"])
        encipher_options_alpha_entry.configure(background="Grey")
        self.encipher_options_alpha_info.set("")
        encipher_options_keyword_entry.state(["disabled"])
        encipher_options_keyword_entry.configure(background="Grey")
        self.encipher_options_keyword_info.set("")
        encipher_options_offset_spin["state"] = "disabled"
        encipher_options_offset_spin.configure(background="Grey")
        # Based on method, re-enables options. (0,) = Caesar, (1,) = Vignere,
        # (2,) = Morse Code (Based off listbox curselection() return)
        if method == (0,):
            encipher_options_alpha_entry.state(["!disabled"])
            encipher_options_offset_spin["state"] = "normal"
            encipher_options_alpha_entry.configure(background="White")
            encipher_options_offset_spin.configure(background="White")
        elif method == (1,):
            encipher_options_alpha_entry.state(["!disabled"])
            encipher_options_keyword_entry.state(["!disabled"])
            encipher_options_alpha_entry.configure(background="White")
            encipher_options_keyword_entry.configure(background="White")
        else:
            pass
        # Temporarily enables the description box, inserts the description, and redisables it.
        encipher_description_box["state"] = "normal"
        encipher_description_box.delete("1.0",END)
        encipher_description_box.insert("1.0", self.cipher_descriptions[method])
        encipher_description_box["state"] = "disabled"

    def encipher_decipher_process(self, type, method, message):
        # Initialise a ciphering object and output variable
        cipher_object = cipher.Cipher(self.encipher_options_alpha_info.get())
        # Identify what the user wants to do and what button was pressed
        if type == "encipher":
            # Note that strings (excluding the value for offset) have their last character removed, as tkinter adds a
            # /n character to the end of strings.
            if method == (0,):
                output = cipher_object.encode_caesar(message[:len(message)-1], self.encipher_options_offset_info.get())
            elif method == (1,):
                output = cipher_object.encode_vignere(message[:len(message)-1], self.encipher_options_keyword_info.get()[:len(self.encipher_options_keyword_info.get())-1])
            elif method == (2,):
                cipher_object = cipher.Morse()
                output = cipher_object.encode_morse(message[:len(message)-1])
            else:
                output = "Error: No method was selected"
        elif type == "decipher":
            if method == (0,):
                output = cipher_object.decode_caesar(message[:len(message)-1], self.encipher_options_offset_info.get())
            elif method == (1,):
                output = cipher_object.decode_vignere(message[:len(message)-1], self.encipher_options_keyword_info.get()[:len(self.encipher_options_keyword_info.get())-1])
            elif method == (2,):
                cipher_object = cipher.Morse()
                output = cipher_object.decode_morse(message[:len(message)-1])
            else:
                output = "Error: No method was selected"
        else:
            output = self.encipher_decipher_tumblr(message)
        # Inserts the message into the output box
        encipher_io_output["state"] = "normal"
        encipher_io_output.delete("1.0",END)
        encipher_io_output.insert("1.0", output)
        encipher_io_output["state"] = "disabled"

    def encipher_decipher_tumblr(self, message):
        """Function which sends a message to Tumblr"""
        # Checks to see if a message and Tumblr URL has been given
        if len(self.encipher_options_tumblr_url_info.get()) == 0 or message == 0:
            return "Error: No Tumblr URL or message was given"
        try:
            # Attempts to create a client using information given by the user
            client = pytumblr.TumblrRestClient(
                self.client_public_key,
                self.client_private_key,
                self.oauth_public,
                self.oauth_private,
            )
            tumblr_output = client.create_text(self.blog_name,state="published", slug=self.encipher_options_tumblr_url_info.get(), text=message, tags=self.encipher_options_tumblr_tags_info.get().split(","))
        except:
            # There's no rule given for the except here, as there are multiple kinds of errors which can occur that
            # aren't feasibly testable (such as Tumblr Servers not being online)
            tumblr_output = """ERROR: Unknown Error when sending information to Tumblr Servers. You may not have given
            a public key/private key/blog name."""
        return tumblr_output


    def pass_generator_select(self,method):
        """Performs specific actions when an enciphering method is selected"""
        # Disable all of the options first, then enable the ones we don't want. We also delete any text present
        pass_options_keyword_one_entry.state(["disabled"])
        pass_options_keyword_one_entry.configure(background="Grey")
        self.pass_options_keyword_one_info.set("")
        pass_options_keyword_two_entry.state(["disabled"])
        self.pass_options_keyword_two_info.set("")
        pass_options_keyword_two_entry.configure(background="Grey")
        pass_options_keyword_three_entry.state(["disabled"])
        self.pass_options_keyword_three_info.set("")
        pass_options_keyword_three_entry.configure(background="Grey")
        pass_options_keyword_four_entry.state(["disabled"])
        self.pass_options_keyword_four_info.set("")
        pass_options_keyword_four_entry.configure(background="Grey")
        pass_options_length_spin["state"] = "disabled"
        pass_options_length_spin.configure(background="Grey")
        # Based on method, re-enables options. (0,) = Zodiac64, (1,) = Zodiac128
        # (2,) = Zodiac256, (3,) = Diceware (Based off listbox curselection() return)
        if method == (0,):
            pass_options_keyword_one_entry.state(["!disabled"])
            pass_options_keyword_one_entry.configure(background="White")
        elif method == (1,):
            pass_options_keyword_one_entry.state(["!disabled"])
            pass_options_keyword_one_entry.configure(background="White")
            pass_options_keyword_two_entry.state(["!disabled"])
            pass_options_keyword_two_entry.configure(background="White")
        elif method == (2,):
            pass_options_keyword_one_entry.state(["!disabled"])
            pass_options_keyword_one_entry.configure(background="White")
            pass_options_keyword_two_entry.state(["!disabled"])
            pass_options_keyword_two_entry.configure(background="White")
            pass_options_keyword_three_entry.state(["!disabled"])
            pass_options_keyword_three_entry.configure(background="White")
            pass_options_keyword_four_entry.state(["!disabled"])
            pass_options_keyword_four_entry.configure(background="White")
        elif method == (3,):
            pass_options_length_spin["state"] = "normal"
            pass_options_length_spin.configure(background="White")
        # Temporarily enables the description box, inserts the description, and re-disables it.
        pass_description_box["state"] = "normal"
        pass_description_box.delete("1.0",END)
        pass_description_box.insert("1.0", self.pass_descriptions[method])
        pass_description_box["state"] = "disabled"

    def pass_generator_process(self, method):
        # Initialise a ciphering object and output variable
        pass_object = cipher.PassGen()
        # Note that strings (excluding offsets) have their last character removed, as tkinter adds a /n character
        # to the end of strings.
        if method == (0,):
            # Note that strings (excluding the value for length) have their last character removed, as tkinter adds a
            # /n character to the end of strings.
            output = pass_object.encode_zodiac64(self.pass_options_keyword_one_info.get()[:len(self.pass_options_keyword_one_info.get())-1])
        elif method == (1,):
            output = pass_object.encode_zodiac128(self.pass_options_keyword_one_info.get()[:len(self.pass_options_keyword_one_info.get())-1], self.pass_options_keyword_two_info.get()[:len(self.pass_options_keyword_two_info.get())-1])
        elif method == (2,):
            output = pass_object.encode_zodiac256(self.pass_options_keyword_one_info.get()[:len(self.pass_options_keyword_one_info.get())-1], self.pass_options_keyword_two_info.get()[:len(self.pass_options_keyword_two_info.get())-1],self.pass_options_keyword_three_info.get()[:len(self.pass_options_keyword_three_info.get())-1], self.pass_options_keyword_four_info.get()[:len(self.pass_options_keyword_four_info.get())-1])
        elif method == (3,):
            output = pass_object.encode_diceware(self.pass_options_length_info.get())
        else:
            output = "Error: No method was selected"
        # Inserts the output into the output box by temporarily enabling it
        pass_io_output["state"] = "normal"
        pass_io_output.delete("1.0",END)
        pass_io_output.insert("1.0", output)
        pass_io_output["state"] = "disabled"


    def options_settings_save(self, client_public, client_private, blog):
        # Removes the disabled flag and any text within so that the program is ready to add text to the error box
        error_box["state"] = "normal"
        error_box.delete("1.0",END)
        try:
            # Saves the client's keys and blog name so they can be used after the options screen is shut down
            self.client_public_key = client_public
            self.client_private_key = client_private
            self.blog_name = blog
            # Remove the previous success/failure message
            self.options_menu_errors = "Save Successful!"
        except AttributeError:
            # This error message is to prevent a program crash and should not happen, even when no data is entered
            # by the user.
            self.options_menu_errors = "Save Failed: Missing 1 or more parameters required. (PROGRAMMING ERROR)"
        # Inserts whatever error message was generated and then re-disables the text box
        error_box.insert("1.0", self.options_menu_errors)
        error_box["state"] = "disabled"

interface = Interface()
interface.main_menu()