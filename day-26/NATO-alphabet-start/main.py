import pandas
alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter:row.code for (index, row) in alphabet_data.iterrows()}

print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

user_input = input("Enter Word: ")

user_input_list = [word.upper() for word in user_input]
print(user_input_list)

converted = [phonetic_dict[letter] for letter in user_input_list]

print(converted)

