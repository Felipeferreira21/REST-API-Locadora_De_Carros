class CarroModel:
    def __init__(self, modelo, ano, marca, diaria, situacao):
        self.modelo = modelo
        self.ano = ano
        self.marca = marca
        self.diaria = diaria
        self.situacao = situacao


    def json(self):
        return {
            'modelo': self.modelo,
            'ano': self.ano,
            'marca': self.marca,
            'diaria': self.diaria,  
            'situacao': self.situacao
                }



