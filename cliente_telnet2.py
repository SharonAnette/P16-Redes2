import telnetlib

# Configuración del cliente
HOST = '127.0.0.0'  # IP de tu servidor
PORT = 5001         # Puerto configurado

# Crear conexión Telnet
try:
    tn = telnetlib.Telnet(HOST, PORT)

    # Recibir el mensaje de bienvenida
    tn.read_until(b"\n").decode('utf-8')

    # Enviar nombre de usuario
    username = input("Ingrese su nombre de u>
    tn.write(username.encode('utf-8') + b"\n>

    # Recibir la solicitud de contraseña
    print(tn.read_until(b"\n", timeout=1).de>

    # Enviar la contraseña
    password = input("Ingrese su contraseña:>
    tn.write(password.encode('utf-8') + b"\n>

    # Recibir el resultado de la autenticaci>
    print(tn.read_all().decode('utf-8'))

except Exception as e:
    print(f"Error al conectar con el servido>
