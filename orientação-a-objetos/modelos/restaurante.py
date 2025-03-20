class Restaurante:
    
    restaurantes = []
    
    def __init__(self, nome, ativo, categoria):
        self._nome = nome.title()
        self._categoria = categoria.upper()
        self._ativo = ativo
        Restaurante.restaurantes.append(self)
        
    def __str__(self):
        return f'{self._nome} | {self._categoria}'

    @classmethod
    def lista_restaurantes(cls):
        print(f"{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'.ljust(25)}")
        for restaurante in cls.restaurantes:   
            print(f'{restaurante._nome.ljust(25)} | {restaurante._categoria.ljust(25)} | {restaurante.status}')
    
    @property
    def status(self):
        return 'Offline' if not self._ativo else 'Online'
    
    def alternar_estado(self):
        self._ativo = not self._ativo


restaurante_praca = Restaurante('Praça', True, 'pizzaria')
restaurante_praca.alternar_estado()
restaurante_pizza = Restaurante('Parque', False, 'churrascaria')

Restaurante.lista_restaurantes()