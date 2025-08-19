# # hear we weite a code that will print the directory path of my system

# # first we need to import the os module

import os

directory_path = '/'  # # in this section we have to select directory

contents = os.listdir(directory_path)

print(contents)

# # with using for loop
# for item in contents:
#     print(item)