import socket

def sending(sock, msg):
    lenght = f'{len(msg):<4}'
    sock.send(f'{lenght}{msg}'.encode())

def reciev(sock):
    recv_msg = int(sock.recv(4).decode().strip())
    data = sock.recv(recv_msg*2).decode()
    return data

sock = socket.socket()
flag = False
while not flag:
    try:
        host = input("Host:")
        if host == "":
            host = 'localhost'
        port = input("Port:")
        if port == "":
            port = 9090
        print('Conection...')
        sock.connect((host, int(port)))
        choise = input('To create an account, enter <1> if you log in to an existing <2>: ')
        sending(sock, choise)

        #Check login
        msg=input("Enter your login:")
        sending(sock, msg)
        proverka = reciev(sock)
        while proverka == 'False':
            print("Wrong user name!")
            msg = input('Enter your login again:')
            sending(sock, msg)
            proverka = reciev(sock)

        #check password
        password=input("Enter password: ")
        sending(sock, password)
        proverka = reciev(sock)
        while proverka == 'False':
            print("Wrong password")
            password = input('Enter password: ')
            sending(sock, password)
            proverka = reciev(sock)

        request = ''
        print('pwd - the full path from the root directory to the current working directory \n'
              'ls - list of files and subdirectories located in a specific directory \n'
              'cat - output the contents of the file \n'
              'echo - overwrite a file, or create a file and write text to it, or add text to a file \n'
              'mkdir - create folder \n'
              'rm - remove file \n'
              'rmdir - remove folder \n'
              'cd - changing the current directory')
        while request != 'exit':
            request = input('~ ')
            sending(sock, request)
            response = reciev(sock)
            if request=='exit':
                print('Stop connection...')
            else:
                print(response)

        flag= True
    except KeyboardInterrupt:
        sock.close()