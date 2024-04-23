import time

class Cronometro:
    
    def __init__(self, hora = 0, minuto = 0, segundo = 0):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo

    def __repr__(self):
        return f'{self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}'
    
    def aumenta(self):
        self.segundo += 1
        if self.segundo >= 60:
            self.segundo = 0
            self.minuto += 1
        elif self.minuto >= 60:
            self.minuto = 0
            self.hora += 1
    
    def show(self):
        while True:
            self.aumenta()
            print(self)
            time.sleep(1)

relogio = Cronometro()
relogio.show()