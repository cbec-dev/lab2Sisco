#Imports

abc = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~'

#Functions

def arrayAString(arr):
    return ''.join(arr)


def enc(llave, mensaje):
    msj_enc = ''
    for i in range(len(mensaje)):
        llave_c = ord(llave[i % len(llave)])
        mensaje_c = ord(mensaje[i % len(mensaje)])
        msj_enc += chr((llave_c + mensaje_c) % 127)
    return msj_enc

def dec(llave, msjEncriptado):
    mensaje = []
    for i, c in enumerate(msjEncriptado):
        llave_c = ord(llave[i % len(llave)])
        enc_c = ord(c)
        mensaje.append(chr((enc_c - llave_c) % 127))
    return arrayAString(mensaje)


def algoritmo_enc(llave, msj, bloque_size):
    msj_enc = ''
    for i in xrange(0, len(msj), bloque_size):
        bloque = msj[i:i+bloque_size]
        msj_enc = msj_enc + enc(llave, bloque)
    return msj_enc

def algoritmo_dec(llave, msj_enc, bloque_size):
    msj_dec = ''
    for i in xrange(0, len(msj_enc), bloque_size):
        bloque = msj_enc[i:i+bloque_size]
        msj_dec = msj_dec + dec(llave, bloque)
    return msj_dec

    


#Main
if __name__ == '__main__':

    #Code
    
    mensaje = raw_input('Ingrese mensaje a encriptar: ')
    llave = raw_input('Ingrese llave: ')
    bloque_size = int(raw_input('Ingrese largo de bloque en bytes: '))
    try:
        number = int(bloque_size)
    except ValueError:
        print("Ingrese un largo de bloque valido")

    msj_enc = algoritmo_enc(llave, mensaje, bloque_size)
    msj_dec = algoritmo_dec(llave, msj_enc, bloque_size)


    print('')
    print('Bloque: ' + str(bloque_size) + " bytes")
    print('mensaje: ' + mensaje)
    print('llave: ' + llave)
    print('mensaje encriptado: ' + msj_enc)
    print('mensaje desencriptado: ' + msj_dec)

    


