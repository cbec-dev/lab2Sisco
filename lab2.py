#Imports



#Functions

def arrayAString(arr):
    return ''.join(arr)

def encriptar(llave, mensaje):
    msj_enc = ''
    for i in range(len(mensaje)):
        llave_c = ord(llave[i % len(llave)])
        mensaje_c = ord(mensaje[i % len(mensaje)])
        msj_enc += chr((llave_c + mensaje_c) % 127)
    return msj_enc

def desencriptar(llave, msjEncriptado):
    mensaje = []
    for i, c in enumerate(msjEncriptado):
        llave_c = ord(llave[i % len(llave)])
        enc_c = ord(c)
        mensaje.append(chr((enc_c - llave_c) % 127))
    return arrayAString(mensaje)


#Main
if __name__ == '__main__':

    #Code
    
    mensaje = "Pantalones de queso"
    llave = "SISCO"

    msj_enc = encriptar(llave, mensaje)
    msj_dec = desencriptar(llave, msj_enc)

    print('mensaje: ' + mensaje)
    print('llave: ' + llave)
    print('mensaje encriptado: ' + msj_enc)
    print('mensaje desencriptado: ' + msj_dec)

