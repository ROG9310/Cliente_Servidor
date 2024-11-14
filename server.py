import socket

def inciar_servidor():
    server= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    server.bind(('localhost',5000))
    server.listen(5)
    print("Servidor TCP escuchando en LH:5000")
    
    while True:
        conexion, direccion = server.accept()
        print(f'Cliente conectado desde {direccion}')
        
        while True:
            mensaje=conexion.recv(1024).decode('utf-8')
            
            if not mensaje:
                break
            
            print(f'Mensaje recibido del cliente: {mensaje}')
            
            if mensaje.upper() =='DESCONEXION':
                print("Cliente solicitó desconexión")
                conexion.close()
                print(f"Cliente {direccion} desconectado")
                break
            else:
                respuesta=mensaje.upper()
                conexion.sendall(respuesta.encode('utf-8'))
                print(f'Enviado al cliente: {respuesta}')

if __name__== "__main__":
    inciar_servidor()