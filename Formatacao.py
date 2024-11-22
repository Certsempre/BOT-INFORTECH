import datetime
import pandas as pd

class Formatacao:
    def __init__(self):
        self._data = datetime.date.today().strftime('%d/%m/%Y')
        self._caminhoNotas = 'C:\\Users\\Pessoal\\Desktop\\Clientes Infortech TEF.xlsx'
        self.sheetnameNotas = 'Clientes sem falha'

    def get_caminhoNotas(self):
        return self._caminhoNotas

    def get_sheetnameNotas(self):
        return self.sheetnameNotas

    def get_data(self):
        return self._data
               
lerPlanilha = pd.read_excel(Formatacao().get_caminhoNotas(), Formatacao().get_sheetnameNotas())


