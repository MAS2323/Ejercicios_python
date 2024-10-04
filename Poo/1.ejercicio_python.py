# Programa de los centros educativos de guinea ecuatorial

class Centro:

    def __init__(self, nombre, categoria, region, ):

        self.nombre = nombre
        self.categoria = categoria
        self.region = region

    def crear_centro(self):
        print('Se ha registrado el', self.categoria, self.nombre,
              'situado en ', self.region)

    def informacion(self, agno, mes, dia):
        self.agno = agno
        self.mes = mes
        self.dia = dia
        print('La matriculas del', self.nombre, 'situado en ',
              self.region, ' estaras abiertas a partir del ', 'agno', self.agno, 'mes', self.mes, ' del dia', self.dia)


miCentro = Centro('Ines Rey Malabo', ' Instituto Nacional', 'Malabo')
miCentro.crear_centro()
miCentro.informacion(2024, 9, 18)
