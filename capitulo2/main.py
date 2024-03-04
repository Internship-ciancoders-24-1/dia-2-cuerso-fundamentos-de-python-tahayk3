import sys
clients = "Cristian,Rene,"

def create_client(client_name):
    global clients
    if client_name not in clients:
        clients += client_name
        _add_comma()
    else: 
        print('Client already is in the client list')

def list_clients():
    global clients
    print(clients)

def update_client(client_name, updated_client_name):
    global clients
    if client_name in clients:
        clients = clients.replace(client_name + ',', update_client_name + ',')
    else:
        print('Client not in client\'s list')

def delete_client(client_name):
    global clients
    if client_name in clients:
        clients = clients.replace(client_name + ',', '')
    else:
        print('Client not in client\'s list')

def search_client(client_name):
    clients_list = clients.split(',')
    for client in clients_list:
        if client != client_name:
            continue
        else:
            return True

def _add_comma():
    global clients
    clients += ","

def _print_welcome():
    print("Bienvenido")
    print("*"*50)
    print("what would you like to do today?")
    print('C reate client')
    print('U update client')
    print('D Delete client')
    print('S Search client')

def _get_client_name():
    client_name = None
    while not  client_name:
        client_name = input('WHat is the client name?')
        if client_name  == 'exit':
            client_name = None
            break
    if not client_name:
        sys.exit()
    return client_name

#Punto de entrada
if __name__ == '__main__':
    _print_welcome()
    command = input()
    command = command.upper()
    if command == 'C':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command =='D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command =='U':
        client_name = _get_client_name()
        update_client_name = input('What is  update the client name?')
        update_client(client_name, update_client_name)
        list_clients()
    elif command =='S':
        client_name = _get_client_name()
        found = search_client(client_name)
        if found:
            print('esta el cliente')
        else:
            print('no esta el cliente')
    else:
        print('Invalid command')

