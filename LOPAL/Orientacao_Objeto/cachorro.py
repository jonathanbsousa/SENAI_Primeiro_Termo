from YKWIM import Cachorro

class CachorroPolicial(Cachorro):
    def procurar_drogas(self):
        print("Procurando drogas...")

def fazer_latir(nome_cachorro):
    nome_cachorro.latir()

rex = CachorroPolicial("Rex", 5)
rex.latir()
rex.procurar_drogas()

fazer_latir(rex)