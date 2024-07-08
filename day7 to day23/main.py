#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
PLACEHOLDER = "[name]"

main_letter = "./Input/Letters/starting_letter.txt"

invited_names_file = "Input/Names/invited_names.txt"

with open(invited_names_file, "r") as names:
    names_list = names.readlines()

with open(main_letter, "r") as letter:
    MAIN_LETTER = letter.read()
    for name in names_list:
        stripped_name = name.strip()
        new_letter = MAIN_LETTER.replace(PLACEHOLDER, name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", "w") as completed_letter:
            completed_letter.write(new_letter)





print(MAIN_LETTER[2])

