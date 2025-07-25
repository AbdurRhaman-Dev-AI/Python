#_______use__\n__escape sequence____to__get___a__new__line______

# x ="""When the sun shine,\n
# we shine together\n
# Told you I'll be here forever\n
# Said "I'll always be your friend"\n
# Took an oath, I'ma stick it out 'til the end\n
# Now that it's rainin' more than ever\n
# Know that we'll still have each other\n
# You can stand under my umbrella\n
# You can stand under my umbrella"""

# print(x)


#__so__we__can__use___[___\"___]___to__prine__""___so___we__can___print___""__in__our__code____

# x = "Marin said \"I love you\" to you"
# print(x)

# and we can print single quote in the string value by using \'

# x = 'Marin said \'I love you\' to you'
# print(x)

# x = 'Marin said \'love you for a thousand years.'
# print(x)


#_______\t__escape sequence____to__get___a__tab______

# X = "Marin\tZarin\tKarin\tSarin"
# print(X)


#________\\__escape sequence____to__get___a__backslash__this__one__(\)_____

# X = "Marin\\Zarin\\Karin\\Sarin"
# print(X)

#_________\b__escape sequence____to__get___a__backspace______
# X = "Marin\bZarin\bKarin\bSarin\b" # this \b backspace escape sequence will remove the last character from the string value how many time we use it
# print(X)


#_________\a__escape sequence____to__get___a__bell______but_____it__dosn't__work_in_my__computer_____

# x = "marin\a"
# print(x)  # this will make a sound if your computer has a speaker and the sound is enabled

#_______\ooo__escape sequence____to__get___a__octal_character______

# x = "marin\101"  # this will print the character that has the octal value of 101 which is 'A'
# print(x)  # Output: marinA


#_______\xhh__escape sequence____to__get___a__hexadecimal_character______

# x = "marin\x41"  # this will print the character that has the hexadecimal value of 41 which is 'A'
# print(x)  # Output: marinA