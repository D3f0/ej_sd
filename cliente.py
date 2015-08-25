# encoding: utf-8
import Pyro4
import sys


def main(argv):
    """
    cliente.py <direccion RFS remoto> <nombre archivo> [nombre archivo destino]
    """
    if argv < 3:
        print("Faltó un argumento")
        return 1
    uri = argv[1]
    proxy = Pyro4.Proxy(uri)

    path = argv[2]
    fuente = open(path, 'r')
    payload = fuente.read()
    fuente.close()

    proxy.write(path, str(payload))



if __name__ == '__main__':
    sys.exit(main(sys.argv))
