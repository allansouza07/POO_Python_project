from modelos.restaurante import Restaurante
from modelos.cardapio.bebidas import Bebidas
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesas import Sobremesa

##ADICIONANDO RESTAURANTE
restaurante_praca = Restaurante('praça', 'Gourmet')

##CRIANDO OS PRATOS EM DIFERENTES CLASSES
bebida_suco = Bebidas('Suco de goiaba', 5.00,'Médio')
prato_bife = Prato('Virado a paulista', 19.00, 'Bife delicioso com batata fritas')
sobremesa_bolo = Sobremesa('Bolo de cenoura',25.00, 'Cenoura')

##ADICIONANDO DESCONTOS NOS PRATOS
bebida_suco.aplicar_desconto
prato_bife.aplicar_desconto
sobremesa_bolo.aplicar_desconto

##ADICIONANDO OS PRATOS DENTRO DA CLASSE RESTAURANTE
restaurante_praca.adicionar_item(prato_bife)
restaurante_praca.adicionar_item(bebida_suco)
restaurante_praca.adicionar_item(sobremesa_bolo)

def main():
    restaurante_praca.listar_cardapio

if __name__ == '__main__':
    main()