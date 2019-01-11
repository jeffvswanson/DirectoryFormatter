# DirectoryFormatterr.py
"""A program to rename files and folders in a directory.
"""

# Testing in "\\CLP-FP02\Data\_CLP ENGINEERING\Standards\References\Test Folder"

import os

def get_pathname():
    pathname = ""
    while not os.path.exists(pathname):
        pathname = input("\nPlease input the directory or file path you wish to format (q to quit): ")
        # Remove quotation marks from around submitted path
        pathname = pathname.replace("\"","")
        # Test if the directory name is valid 
        # If yes, continue, else ask for another input.
        if pathname == 'q':
            quit()
        elif os.path.isdir(pathname) | os.path.isfile(pathname):
            break
        else:
            print("{} is not a file or directory".format(pathname))
    return pathname

def format_pathname(pathname, name_to_format):
    special_characters = ' ~!@#$%^&*()`;<>?,[]{}"\'|/+=\\'
    # Don't change anything after and including the last period, filetype designator.
    # Don't change anything above the chosen directory.
    
    # Replace every letter after a space with a capital letter.
    # Do not use .title() or other methods as it messes up consecutive capitalization, that is, acronyms like ABC become Abc.
    name_to_format = ''.join(word[0].upper() + word[1:] for word in name_to_format.split())
    # for each character in special characters
        # while character in pathname
            # Replace the symbol
    for _, character in enumerate(special_characters):
        while character in name_to_format:
            if character == '&':
                name_to_format = name_to_format.replace(character, "And")
            elif character == '(':
                name_to_format = name_to_format.replace(character, '_')
            else:
                name_to_format = name_to_format.replace(character, "")
    pathname = os.path.join(pathname, name_to_format)
    return pathname
def main():

# Input the name of the directory you want to recursively search
# Ask if the user wants the search to be recursive or just that directory
# Read through the directory
# Remove all spaces, if a space - capitalize the following character and remove the space
# Remove any special character other than: dash, '-'; underscore, '_'; and period, '.'
# If the special character is an opening parentheses, '(', replace it with an underscore
# Go through any subdirectories and repeat 2 - 4. 
    print("This program formats a directory and all its subdirectories and files according to standardized file naming conventions.")
    print("\nFormatted files will have: all spaces removed; file and folder names rewritten in CamelCase; and all special characters except for underscore, '_', dash, '-', and period, '.' removed.")
    
    pathname = get_pathname()
    # dirpath needed as os.walk returns a tuple of three.
    for dirpath, subdirs, files in os.walk(pathname, topdown=False):
        for filename in files:
            original_pathname = os.path.join(dirpath, filename)
            new_pathname = format_pathname(dirpath, filename)
            os.replace(original_pathname, new_pathname)
        new_folder_name = format_pathname(os.path.dirname(dirpath), os.path.basename(dirpath))
        os.replace(dirpath, new_folder_name)

    print("All files and folders have been formatted.")

main()