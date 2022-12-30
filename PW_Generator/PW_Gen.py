from ntpath import join

import numpy as np
import string

class Generator(object):
    def __init__(self,reshuffle) -> None:
        self.reshuffle_bool = reshuffle
        self.yes_choices = ['yes', 'y', '']
        self.no_choices = ['no', 'n']
    pass

    def PW_Generator_prep(self):
        while True:
            amount_char = input('Please insert desired amount of characters in password: ')
            if not amount_char.isdigit():
                print("Sorry, only integes are allowed. Please try again")
            elif int(amount_char) <= 0:
                print("Sorry, no numbers below one. Please try again.")
            else:
                break
        while True:
            caps_reply = input('Does the password also require capital letters? Please answer with yes or no. ')
            if caps_reply.lower() in self.yes_choices:
                caps_bool = True
                break
            elif caps_reply.lower() in self.no_choices:
                caps_bool = False
                break
            else:
                print("Please answer with yes or no")
        while True:
            numbers_reply = input('Does the password require numbers (0-9). Please answer with yes or no. ')
            if numbers_reply.lower() in self.yes_choices:
                numbers_bool = True
                while True:
                    numbers_char = input('What is the minimum amount of numbers (0-{})? '.format(amount_char))
                    if not numbers_char.isdigit():
                        print("Sorry, only integes are allowed. Please try again")
                    elif (int(numbers_char) >= 0 and int(numbers_char) <= int(amount_char)):   
                        break
                    else:
                        print("Please enter a number between 0 and {}".format(amount_char))
                break

            elif numbers_reply.lower() in self.no_choices:
                numbers_bool = False
                numbers_char = 0
                break
            else:
                print("Please answer with yes or no")
        while True:
            specs_reply = input('Does the password also require special signs? Please answer with yes or no. ')
            if specs_reply.lower() in self.yes_choices:
                specs_bool = True
                break
            elif specs_reply.lower() in self.no_choices:
                specs_bool = False
                break
            else:
                print("Please answer with yes or no")
        return amount_char, caps_bool, numbers_bool, numbers_char, specs_bool

    def PW_Generator(self, prep_values): #amount_char, caps_bool, numbers_bool, numbers_char, specs_bool
        amount_char, caps_bool, numbers_bool, numbers_char, specs_bool = prep_values
        rng = np.random.default_rng()
        generated_pw_arr = []

        if caps_bool:
            alphabet = string.ascii_letters
        else:
            alphabet = string.ascii_lowercase
    
        for i in range(int(amount_char)):
            idx = rng.integers(low=0, high=len(alphabet))
            generated_pw_arr.append(alphabet[idx])
    
        if specs_bool:
            spec_signs = string.punctuation
            generated_specs = []
            for i in range(rng.integers(low=1, high=np.ceil(int(amount_char)/2))):
                idx = rng.integers(low=0,high=len(spec_signs))
                generated_specs.append(spec_signs[idx])
            char_to_int_vec = np.random.choice(range(0,int(amount_char)),len(generated_specs),replace=False).tolist()
            for i in char_to_int_vec:
                generated_pw_arr[i] = str(generated_specs[0])
                generated_specs.remove(generated_specs[0])

        if numbers_bool:
            generated_numbs = []
            for i in range(int(numbers_char)):
                idx = rng.integers(low=0,high=len(generated_pw_arr))
                generated_numbs.append(idx)
            char_to_int_vec = np.random.choice(range(0,int(amount_char)),len(generated_numbs),replace=False).tolist()
            for i in char_to_int_vec:
                generated_pw_arr[i] = str(generated_numbs[0])
                generated_numbs.remove(generated_numbs[0])

        generated_pw = ''.join(generated_pw_arr)
        generated_pw, self.reshuffle_bool = self.Reshuffle(generated_pw)
        return generated_pw, self.reshuffle_bool

    def Reshuffle(self, password):
        print("Your password is: {}.\n".format(password))
        reshuf = input("Would you like another one? Please answer with yes or no. ")
        while True:
            if reshuf.lower() in self.yes_choices:
                reshuf_bool = True
                break
            elif reshuf.lower() in self.no_choices:
                reshuf_bool = False
                break
            else:
                print("Please answer with yes or no")
                reshuf = input("Would you like another one? Please answer with yes or no. ")
        return password, reshuf_bool
    
    def run(self):
        password_prep = self.PW_Generator_prep()
        password, self.reshuffle_bool = self.PW_Generator(password_prep)
        while True:
            if self.reshuffle_bool:
                password, self.reshuffle_bool = self.PW_Generator(password_prep)
            else:
                break
        return password


