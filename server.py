import socket


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(('localhost', 5000))
    this_name = 'server'
    that_name = 'client'
    server_socket.listen()
    print("Server is running...")

    try:
        while True:
            client_socket, adr = server_socket.accept()
            # обмен именами
            client_socket.send(this_name.encode())
            new_name = client_socket.recv(4096).decode()
            if new_name:
                that_name = new_name
                del new_name
            print('Connection from', adr)
            while True:
                answer = client_socket.recv(4096)

                if not answer:
                    print('No answer, waiting for another connection')
                    break
                else:
                    print(that_name, answer.decode())
                    response = input(this_name + ': ')
                    #if response == '!quit':
                    #    break
                    client_socket.send(response.encode())
            client_socket.close()
    finally:
        server_socket.close()


if __name__ == "__main__":
    main()
