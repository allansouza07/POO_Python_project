from modelos.restaurante import Restaurante
from modelos.cardapio.bebidas import Bebidas
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesas import Sobremesa

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebidas('Suco de goiaba', 5.00,'Médio')
prato_bife = Prato('Virado a paulista', 19.00, 'Bife delicioso com batata fritas')
sobremesa_bolo = Sobremesa('Bolo de cenoura',25.00, 'Cenoura')
def main():
    print(bebida_suco)
    print(prato_bife)
    print(sobremesa_bolo)

if __name__ == '__main__':
    main()