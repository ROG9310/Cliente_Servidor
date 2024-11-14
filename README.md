# Cliente_Servidor


SERVIDOR TCP

Para iniciar el servicio TCP, es necesario hacer uso de la librería Socket, 
para que el localhost pueda recibir peticiones, haciendo la simulación de un servidor.

En nuestro caso usaremos el puerto 5000, para poder asignarle el puerto es neseraio hacer uso de la función bind pasando los dos parametros 
al servidor (localhost) y el puerto donde recibirá las peticiones (5000).

Una vez parametrizado haremos que el seridor escuche 5 peticiones simultaneas

Una vez iniciado el servidor, entrará en un bucle esperando las peticiones de los clientes.
Este recibirá los mensajes del cliente con una colación de datos UTF-8 para que acepte caracteres especiales del español.

Si existe un mensaje del clinete, el servidor devolverá una respuesta al clinete,
en caso de que el mensaje sea 'DESCONEXION', el servidor hará caso a la petición de desconexión del cliente notificando en consola la desconexión y 
el clinete de la petición.


CLIENTE TCP

Primero haciendo uso de la librería Socket, daremos inicio al cliente y lo conectaremos al servidor quye hemos creado anteriormente, pasando como parametros la dirección ip y el puerto.
en nuestro caso el localhost y el puerto 5000.

Si existe la conexión entrará a un bucle while para empezar a enviar los mensajes al servidor.
Haciendo la validación del mensaje, donde si el cliente envia 'DESCONEXION' esté mandrá el mensaje al servidor y dará por finalizada la conexión al servidor,
en caso de no hacer la petición de cerrar conexión, entonces recibirá la respuesta del servidor.


###     RENE OJEDA GALVAN    ###


