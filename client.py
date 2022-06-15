import socket


def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    this_name = "best_client"
    that_name = 'server'
    while True:  # connect
        try:
            client_socket.connect(('localhost', 5000))
        except ConnectionRefusedError:
            ask = input('Connection refused, retry? y/n \n')
            if ask == 'n':
                client_socket.close()
                return
        break

    # обмен именами
    new_name = client_socket.recv(4096).decode()
    if new_name:
        that_name.replace('', new_name)
    client_socket.send(this_name.encode())

    while True:  # chat
        message = input(this_name + ": ")
        if message == '!quit':
            client_socket.send('is leaving'.encode())
            client_socket.close()
            break
        client_socket.send(message.encode())
        answer = client_socket.recv(4096).decode()
        print(that_name, answer)
    return


if __name__ == "__main__":
    main()
