pass_file = "/Users/sheharyarmeghani/Documents/password.txt"

def encrypt(password):
    encrypted = ''
    for char in password:
        encrypted = encrypted + chr( ord(char) + 5)
    return encrypted

def decrypt(password):
    decrypted = ''
    for char in password:
        decrypted = decrypted + chr( ord(char) - 5)
    return decrypted




def format_file(read_file):
    app_pass = {}
    line = read_file.readline()

    while line != '' :
        app = line.strip().split(':')[0]
        password = read_file.readline().strip()
        app_pass[app] = decrypt(password)
        read_file.readline()
        line = read_file.readline()
    
    return app_pass







def read_pass(pass_file):
    read_file = open(pass_file , 'r')
    line = read_file.readline()
    if line == '' or line == '\n':
        print('No Passwords')
        read_file.close()
        return 1
    else:
        read_file.readline()
        app_pass = format_file(read_file)
        read_file.close()
        check = (input("Enter the name of account you want the password for:  ")).lower()
        if check in app_pass:
            print(app_pass[check])
            return 0
        else:
            print("No such account.")
            return 0
            
        
    
def write_pass(pass_file):

    read_file  = open(pass_file , 'r')
    line = read_file.readline()
    if line == '' or line == '\n':
        read_file.close()
        write_file = open(pass_file, 'w')
        set_master = input("Set your master password:  ")
        if set_master == input("Confirm master password:  "):
            write_file.write(encrypt(set_master) + '\n' + '\n')
            write_file.close()
        else:
            print("Not matching.")
            return 1

    read_file.close()


    add_file = open(pass_file , 'a')
    app = (input("Enter name of account you want to add password for: ")).lower()
    password = input("Enter password for account: ")
    if password == input("Confirm password: "):
        add_file.write(app + ':'  + '\n' + encrypt(password) + '\n' + '\n')
        add_file.close()
        return 0 
    else:
        print("Not matching.")
        add_file.close()
        return 1




allow = 1
read_file = open(pass_file , 'r')
line = read_file.readline()
if line != '' and line != '\n':
    master = decrypt(line.strip())
    master_input = input("Please enter master password.  ")
    if master != master_input:
        print("Wrong master password.")
        read_file.close()
        allow = 0
read_file.close()

while allow == 1:
    

    command = (input("Do you want to add or view a password(a,v). Enter 1 to exit  ")).lower()
    while command != 'v' and command != 'a' and command != '1':
        command = (input("Invalid input, Do you want to add or view a password(a,v). Enter 1 to exit  ")).lower()
    
    if command == '1':
        break
    if command == 'v':
        read_pass(pass_file)
    else:
        write_pass(pass_file)


    


