# encoding: utf-8
import os
import sys
import Pyro4


class FileExistsError(Exception):
    pass

class RFS(object):
    def __init__(self, path):
        """
        @parm path La ruta dónde trabaja el servdor
        """
        self.path = path

    def write(self, name, payload):
        ruta_real = os.path.join(self.path, name)
        if os.path.exists(ruta_real):
            raise FileExistsError("El archivo {} ya existe".format(ruta_real))
        print(ruta_real)
        archivo = open(ruta_real, 'w')
        archivo.write(payload)
        archivo.close()

def main(argv):
    if len(argv) != 2:
        print("Faltó un argumento")
        return 1

    work_path = os.path.abspath(argv[1])
    print("Estoy trabajando en {0}".format(work_path))
    rfs = RFS(work_path)

    Pyro4.Daemon.serveSimple({
        rfs: "RFS"
    }, ns=False)

if __name__ == '__main__':
    sys.exit(main(sys.argv))
