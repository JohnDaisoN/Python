from pathlib import Path
flag = True
string = ''
while flag:
    name = input("Enter a user name, you idiot")
    string += name + '\n'
    comm = input('Is the user list complete') 
    if comm == 'yes':
        flag = False

path = Path('guest_book.txt')
path.write_text(string)


