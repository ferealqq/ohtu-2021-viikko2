class Varasto:
    def __init__(self, tilavuus, alku_saldo = 0):
        if tilavuus > 0.0:
            self.tilavuus = tilavuus
        else:
            # virheellinen, nollataan
            self.tilavuus = 0.0
        
        if alku_saldo < 0.0:
            # virheellinen, nollataan
            self.saldo = 0.0
        elif alku_saldo <= tilavuus:
            # mahtuu
            self.saldo = alku_saldo
        else:
            # täyteen ja ylimäärä hukkaan!
            self.saldo = tilavuus

    # huom: ominaisuus voidaan myös laskea. Ei tarvita erillistä kenttää viela_tilaa tms.
    def paljonko_mahtuu(self):
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        if maara < 0:
            return
        if maara <= self.paljonko_mahtuu():
            self.saldo = self.saldo + maara
        else:
            self.saldo = self.tilavuus

    def ota_varastosta(self, maara):
        if maara < 0:
            return 0.0
        if maara > self.saldo: 
            kaiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiikkimitävoidaan = self.saldo
            self.saldo = 0.0

            return kaiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiikkimitävoidaan

        self.saldo = self.saldo - maara

        return maara

    def nested_blocks(self,one, two ,three, four, five, six,seven, eigth, nine, ten, eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen, twenty):
        lst = range(100)
        for i in lst:
            for j in lst:
                for k in lst:
                    print(f"{i} {j} {k}")
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        useless_line = True
        # twenty useless lines of code
        # twenty useless lines of code
        # twenty useless lines of code
        # twenty useless lines of code
        # twenty useless lines of code
        # twenty useless lines of code
        # twenty useless lines of code
        # twenty useless lines of code
        # twenty useless lines of code
        # twenty useless lines of code
        # twenty useless lines of code
        # twenty useless lines of code
        # twenty useless lines of code
        # twenty useless lines of code
        # twenty useless lines of code
        # twenty useless lines of code
        # twenty useless lines of code
        # twenty useless lines of code
        # twenty useless lines of code
        # twenty useless lines of code
        # twenty useless lines of code
        # twenty useless lines of code

        return "nested_blocks()"            
            

    def __str__(self):
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
