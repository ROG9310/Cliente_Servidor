import socket

def iniciar_cliente():
    cliente=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    cliente.connect(('localhost',5000))
    print("Conectado al servidor en LH:5000")
    
    while True:
        mensaje = input("Ingresar mensaje o DESCONEXION para salir: ")
        cliente.sendall(mensaje.encode('utf-8'))
        
        if mensaje.upper() == 'DESCONEXION':
            print("Solicitud de desconexion inicada.")
            cliente.close()
            break
        respuesta= cliente.recv(1024).decode('utf-8')
        print(f'Respuesta del servidos {respuesta}')
if __name__== '__main__':
    iniciar_cliente()