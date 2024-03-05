import sys
clients = [
    {
        'name': 'Pablo',
        'company': 'Google',
        'email': 'asd@gmail.com',
        'position': 'Software enginner',
    },
    {
        'name': 'Valeria',
        'company': 'Facebook',
        'email': 'asd@gmail.com',
        'position': 'Data enginner',
    },

]
def create_client(client):
    global clients
    if client not in clients:
        clients.append(client)
    else: 
        print('Client already is in the client list')

def list_clients():
    for idx, client in enumerate(clients):
        print('{udi} | {name} |{company} |{email} |{position}'.format(
            udi= idx,
            name = client['name'],
            company = client['company'],
            email = client['email'],
            position = client['position']))


def update_client(client_id, updated_client):
    global clients
    if client_id < len(clients):
        clients[client_id] = updated_client
    else:
        print('Client not in client\'s list')


def delete_client(client_id):
    global clients
    if client_id < len(clients):
        del clients[client_id]
    else:
        print('Id not found')


def search_client(client_name):
    for client in clients:
        if client['name'].lower() == client_name.lower():
            return client
    return None



def _print_welcome():
    print("Bienvenido")
    print("*"*50)
    print("what would you like to do today?")
    print('C reate client')
    print('L list client')
    print('U update client')
    print('D Delete client')
    print('S Search client')

def _get_client_field(field_name):
    field = None
    while not  field:
        field = input('What is the client {}?'.format(field_name))
    return field


def _get_client_name():
    client_name = None
    while not  client_name:
        client_name = input('What is the client name?')
        if client_name  == 'exit':
            client_name = None
            break
    if not client_name:
        sys.exit()
    return client_name

def _get_client_id():
    client_id = None
    while client_id is None:
        try:
            client_id = int(input('Enter the client ID: '))
        except ValueError:
            print('Invalid ID. Please enter a number.')
    return client_id

#Punto de entrada
if __name__ == '__main__':
    _print_welcome()
    command = input()
    command = command.upper()
    if command == 'C':
        client = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position'),
        }
        create_client(client)
        list_clients()
    elif command =='D':
        client_id = _get_client_id()
        delete_client(client_id)
        list_clients()


    elif command =='L':
        list_clients()
    elif command =='U':
        client_id = int(input('Enter the client ID to update: '))
        updated_client = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position'),
        }
        update_client(client_id, updated_client)
        list_clients()

    elif command == 'S':
        client_name = _get_client_name()
        found_client = search_client(client_name)
        if found_client:
            print('Client found:', found_client)
        else:
            print('Client not found')


    else:
        print('Invalid command')

