from modelos.restaurante import Restaurante
from modelos.cardapio.bebidas import Bebidas
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesas import Sobremesa



##RESTAURANTE DO BAHIANO
restaurante_bahiano = Restaurante('Bahiano', 'Comida caseira')
##CRIANDO OS PRATOS EM DIFERENTES CLASSES
bebida_suco = Bebidas('Suco de limão', 5.00,'Médio')
bebida_suco_goiaba = Bebidas('Suco de goiaba', 5.00,'Médio')
prato_moqueca = Prato('Moqueca', 25.00, 'Moqueca apimentada e com muito molho bahiano')
prato_bife = Prato('Bife com batata fritas', 19.00, 'Bife delicioso com batata fritas')
sobremesa_bolo = Sobremesa('Bolo de cenoura',25.00, 'Cenoura')
##ADICIONANDO DESCONTOS NOS PRATOS
bebida_suco.aplicar_desconto
bebida_suco_goiaba.aplicar_desconto
prato_bife.aplicar_desconto
prato_moqueca.aplicar_desconto
sobremesa_bolo.aplicar_desconto
##ADICIONANDO OS PRATOS DENTRO DA CLASSE RESTAURANTE
restaurante_bahiano.adicionar_item(prato_bife)
restaurante_bahiano.adicionar_item(prato_moqueca)
restaurante_bahiano.adicionar_item(bebida_suco)
restaurante_bahiano.adicionar_item(bebida_suco_goiaba)
restaurante_bahiano.adicionar_item(sobremesa_bolo) 


##RESTAURNATE NATURAL
restaurante_natural = Restaurante('Natural','Comida vegana')
##CRIANDO OS PRATOS EM DIFERENTES CLASSES
bebida_agua = Bebidas('Água gaseificada', 10.00,'Médio')
bebida_suco_limao = Bebidas('Suco de limão', 17.00,'Médio')
prato_salada = Prato('Salada', 20.00, 'Salada natural com variedades de nutrientes')
prato_cereal = Prato('Cereal', 14.00, 'Cereal light')
sobremesa_salada_frutas = Sobremesa('Salada de frutas',45.00, 'Salada de frutas com frutas como maça, banana e manga')
##ADICIONANDO DESCONTOS NOS PRATOS
bebida_agua.aplicar_desconto
bebida_suco_limao.aplicar_desconto
prato_salada.aplicar_desconto
prato_cereal.aplicar_desconto
sobremesa_salada_frutas.aplicar_desconto
##ADICIONANDO OS PRATOS DENTRO DA CLASSE RESTAURANTE
restaurante_natural.adicionar_item(bebida_agua)
restaurante_natural.adicionar_item(bebida_suco_limao)
restaurante_natural.adicionar_item(prato_salada)
restaurante_natural.adicionar_item(prato_cereal)
restaurante_natural.adicionar_item(sobremesa_salada_frutas) 


##BURGUER RESTAURANTE
burguer_restaurante = Restaurante('Burguer', 'Fast-Food')
##CRIANDO OS PRATOS EM DIFERENTES CLASSES
refrigerante = Bebidas('Coca-Cola', 5.00,'Pequeno')
prato_xsalada = Prato('X-salada', 12.00, 'X-salada delicioso')
prato_xbacon = Prato('X-bacon', 14.00, 'X-bacon delicioso')
sobremesa_casquinha = Sobremesa('Casquinha Mista',4.00, 'Baunilha e chocolate')
##ADICIONANDO DESCONTOS NOS PRATOS
refrigerante.aplicar_desconto
prato_xsalada.aplicar_desconto
prato_xbacon.aplicar_desconto
sobremesa_casquinha.aplicar_desconto
##ADICIONANDO OS PRATOS DENTRO DA CLASSE RESTAURANTE
burguer_restaurante.adicionar_item(refrigerante)
burguer_restaurante.adicionar_item(prato_xsalada)
burguer_restaurante.adicionar_item(prato_xbacon)
burguer_restaurante.adicionar_item(sobremesa_casquinha)


