"""
Los decoradores se utilizan para modificar el comportamiento de una funcion, sin modificarla internamente.
Por lo general, la funcion interna del decorador se llama wrapper.
si o si, el decorador necesita como parametro, la funcion a modificar.
ademas de modificar el comportamiento, el decorar puede permitir o negar el acceso a la funcion que esta
siendo modificada por el decorador
"""


#ejemplo1
PASSWORD = '12345'

def password_required(func):
    def wrapper():
        password = input("Cual es tu contraseña?")
        if password == PASSWORD:
            return func()
        else:
            print('La contraseña no es correcta')
    
    return wrapper

@password_required
def needs_password():
    print('La contraseña es correcta')


#ejemplo2
def upper(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper    

@upper
def say_my_name(name):
    return 'Hola'+ name

if __name__ == '__main__':
    print(say_my_name('Cristian'))

